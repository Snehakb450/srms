from django.shortcuts import render,redirect
from admin1.models import Notice,Class,Student,Fee,Results,Attendance,Month,Subject
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from django.db.models import Q,Sum
from django.http import JsonResponse,HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import io
# from .pdf import html2pdf


# Create your views here.
def get_student_master(request):
     return render(request,"student/student_master.html")
     
def get_verify_otp(request):
     if request.method=="POST":
        otp=request.POST['sotp']
        s_id=request.session['student_id']
        data=Student.objects.get(id=s_id)
        if otp==data.otp:
            Student.objects.filter(id=s_id).update(status='active')
            return redirect('student:student_dash')
        else:
            return render(request,"student/verify_otp.html",{ 'mes':'invalid otp'})
    
     return render(request,"student/verify_otp.html")

def get_student_home(request):
     if request.method=='POST':
          user=request.POST['user']
          pwd=request.POST['pwd']
          try:
               student=Student.objects.get(student_email=user,student_password=pwd)
               request.session['student_id']=student.id
               return redirect('student:student_dash')
          except Student.DoesNotExist:
               return render(request,"student/student_register.html",{'message':'Login failed'})
          
     return render(request,"student/student_home.html")

def get_student_dash(request):
     if 'student_id' in request.session:
          s_id=request.session['student_id']
          student_details=Student.objects.get(id=s_id) 
          
          return render(request,"student/student_dash.html",{ 'data': student_details})
     else:
          return redirect('student:student_home')
     
def logoutstudent(request):
     del request.session['student_id']
     return redirect('student:student_home') 
   
def get_student_forgot(request):
     mes=""
     if request.method=='POST':
          mail=request.POST['emailorUsername']
          student_exist=Student.objects.filter(student_email=mail).exists()
          a=Student.objects.get(student_email=mail) 
          if not student_exist:
               mes="You don't have an account." 
          
          else:
               sotp=randint(1000,9999)
               send_mail('Please verify yout otp',
                         'Verify your otp and change your password'+str(sotp),
                         settings.EMAIL_HOST_USER,
                         [mail],fail_silently=False,
               )
               
               Student.objects.filter(id=a.id).update(student_password=str(sotp))
               return redirect('student:student_home')
    
     return render(request,"student/student_forgot.html")

def get_notices(request):
     notice=Notice.objects.all() 
     return render(request,"student/notices.html",{'notices':notice})
     
def get_change_pwd(request):
     if request.method=='POST':     
          current_pwd=request.POST['inputPsw']
          new_pwd=request.POST['inputPsw1']
          student_id=request.session['student_id']
          data=Student.objects.get(id=student_id) 
          if current_pwd==data.student_password : 
               Student.objects.filter(id=student_id).update(student_password=new_pwd) 
               return redirect('student:student_dash')  
                       
     return render(request,"student/change_pwd.html") 

def get_fees(request):   
    student_id = request.session['student_id']
    data = Student.objects.get(id=student_id)
    fees=Fee.objects.get(class_name=data.student_class) 
    return render (request,"student/fees.html",{'fee': fees})

def get_attend(request):
    s_id=request.session['student_id'] 

    months = Month.objects.all()

    month_data = {}
    for month in months:
        month_data[month.month] = month.total

    attendance_data = {}
    attendances = Attendance.objects.filter(student_id=s_id)
    for attendance in attendances:
        attendance_data[attendance.month] = {
            'day' + str(i): getattr(attendance, 'day' + str(i))
            for i in range(1, 32)
        }

    context = {
        'months': months,
        'attendance_data': attendance_data,
        'month_data': month_data,
        'id':s_id,
    }
    return render(request, 'student/attend.html', context) 

def fetch_attendance(request):
    if request.method == 'GET':
        student_id = request.GET.get('student_id')
        month = request.GET.get('month')

        try:
            attendance = Attendance.objects.get(student_id=student_id, month=month)
        except Attendance.DoesNotExist:
            return JsonResponse({'error': 'Attendance not found for the selected student and month'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

        try:
            # Fetch the total from the Month table for the selected month
            month_obj = Month.objects.get(month=month)
            
        except Month.DoesNotExist:
            # If the total is not found, set it to 0
            total = 0
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

        # Create a dictionary to store the attendance data and the total
        attendance_data = {
            'month': month,
            'day1': attendance.day1,
                'day2': attendance.day2,
                'day3': attendance.day3,
                'day4': attendance.day4,
                'day5': attendance.day5,
                'day6': attendance.day6,
                'day7': attendance.day7,
                'day8': attendance.day8,
                'day9': attendance.day9,
                'day10': attendance.day10,
                'day11': attendance.day11,
                'day12': attendance.day12,
                'day13': attendance.day13,
                'day14': attendance.day14,
                'day15': attendance.day15,
                'day16': attendance.day16,
                'day17': attendance.day17,
                'day18': attendance.day18,
                'day19': attendance.day19,
                'day20': attendance.day20,
                'day21': attendance.day21,
                'day22': attendance.day22,
                'day23': attendance.day23,
                'day24': attendance.day24,
                'day25': attendance.day25,
                'day26': attendance.day26,
                'day27': attendance.day27,
                'day28': attendance.day28,
                'day29': attendance.day29,
                'day30': attendance.day30,
            'day31': attendance.day31,
        }

        # Return the attendance data and the total in the response
        return JsonResponse({'attendance_data': attendance_data})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def fetch_total(request):
    if request.method == 'GET':
        selected_month = request.GET.get('month')

        # Fetch the total value from the Month model based on the selected month
        total_working_days = 0
        if selected_month:
            try:
                month = Month.objects.get(id=selected_month)
                total_working_days = month.total 
            except Month.DoesNotExist:
                # Handle the case when the selected month does not exist in the Month model
                pass

        return JsonResponse({'total_working_days': total_working_days})
    
def get_results(request):
    if 'student_id' in request.session:
        s_id=request.session['student_id'] 
        s=Student.objects.get(id=s_id) 
        clss=Class.objects.filter(class_name=s.student_class)  
     
    return render(request, "student/results.html",{'class_details':clss,'id':s_id})  

def fetch_subjects_and_results(request):
    if request.method == 'GET':
        student_id = request.GET.get('student_id')
        semester_id = request.GET.get('semester')

        if not student_id or not semester_id:
            return JsonResponse({'error': 'Student ID or Semester not provided'})

        subjects = Subject.objects.filter(class_id=semester_id)

        results = Results.objects.filter(student_roll=student_id, class_id=semester_id)

        subject_data = []
        result_data = []

        for subject in subjects:
            subject_data.append({
                'subject_name': subject.class_sub,
                'subject_id': subject.class_subid,
                'credits': subject.credit,
            })

        for result in results:
            result_data.append({
                'subject_id': result.sub_id.class_subid,
                'marks': result.marks,
                'total_marks': result.total_marks, 
                'grade': result.grade,
                'grade_point':result.grade_point, 
            })
            

        data = {
            'subjects': subject_data,
            'results': result_data,
        }

        return JsonResponse(data)


def pdf(request,c_id):
    student_id = request.session.get('student_id')
    
    if student_id:
        class_details = Class.objects.get(id=c_id)
        data=Student.objects.get(id=student_id) 
        id=data.student_sem
        result_data = [
           
        ]
        
        context = {
            'class_details': class_details,
            'id': student_id,
            'classid':c_id,
            'result_data': result_data,
            'data':data,
            'id':id,
            
        }
        return render(request, 'student/pdf.html', context)
    else:
        
        pass
    
    pdf=html2pdf('student/pdf.html') 
    
    return HttpResponse(pdf,content_type="application/pdf") 
    

# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.template import Context
# from xhtml2pdf import pisa

# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = io.BytesIO()
#     pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None

# def generate_pdf(request):
#     template = get_template('student/pdf.html')  # Use your actual template path
#     context = {
        
        
#     }
#     result_data = fetch_subjects_and_results(request)
#     print(result_data) 
#     html = template.render(context)
    
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="exam_results.pdf"'
    
#     pdf = pisa.pisaDocument(html, dest=response)
#     if pdf.err:
#         return HttpResponse('PDF generation error', status=500)
    
#     return response
