from django.shortcuts import render,redirect,render
from admin1.models import Staff,Class,Subject,Notice,Fee,Student,Results,Attendance ,Main,Month
from django.http import JsonResponse
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from django.shortcuts import render


# Create your views here.
def get_admin_master(request):
     return render(request,"admin1/admin_master.html")

def get_admin1_home(request):
     if request.method=='POST':
          username=request.POST['username']
          password=request.POST['password']
          try:
               admin=Staff.objects.get(admin_email=username,admin_password=password)
               request.session['admin_id']=admin.id
               if admin.status=="active":
                    return redirect('admin1:dashboard')
          except Staff.DoesNotExist: 
               return render(request,"admin1/admin1_home.html",{'message':'Login failed'})
          
     return render(request,"admin1/admin1_home.html")

def get_register(request):
     ms=""
     if request.method=='POST':
          name=request.POST['fullname']
          adminid=request.POST['adminid']
          gender=request.POST['gender']
          dob=request.POST['dob']
          email=request.POST['email']
          admin_exist=Staff.objects.filter(admin_email=email).exists()
          if not admin_exist:
               otp=randint(1000,9999)
               send_mail('Please verify your otp',
                    'This is your password. Login using this then change the password' + str(otp),
                    settings.EMAIL_HOST_USER,
                    [email],fail_silently=False,
               )
               admin=Staff(admin_name=name,admin_id=adminid,admin_gender=gender,admin_dob=dob,admin_email=email,admin_password=str(otp))
               admin.save()
               admin_data=Staff.objects.get(admin_email=email)
               request.session['admin_id']=admin_data.id
               
               return redirect('admin1:admin1_home')
          else:
               ms="Admin already exist"
     return render(request,"admin1/register.html",{'mse':ms})

def get_admin1_forgot(request):
     mes=""
     if request.method=='POST':
          mail=request.POST['emailorUsername']
          admin_exist=Staff.objects.filter(admin_email=mail).exists()
          a=Staff.objects.get(admin_email=mail) 
          if not admin_exist:
               mes="You don't have an account." 
          
          else:
               sotp=randint(1000,9999)
               send_mail('Please verify yout otp',
                         'Verify your otp and change your password'+str(sotp),
                         settings.EMAIL_HOST_USER,
                         [mail],fail_silently=False,
               )
               
               Staff.objects.filter(id=a.id).update(admin_password=str(sotp))
               return redirect('admin1:admin1_home')  
                        
     return render(request,"admin1/admin1_forgot.html") 
   
def get_change(request):
     if request.method=='POST':     
          current_pwd=request.POST['pwd7']
          new_pwd=request.POST['pwd8']
          admin_id=request.session['admin_id']
          data=Staff.objects.get(id=admin_id)
          if current_pwd==data.admin_password : 
               Staff.objects.filter(id=admin_id).update(admin_password=new_pwd) 
               return redirect('admin1:profile_admin')               
     return render(request,"admin1/change.html")  

def get_edit_profile(request,a_id): 
     if request.method=='POST':
          name=request.POST['name1'] 
          dob=request.POST['dob1']
          email=request.POST['mail']
          
          Staff.objects.filter(id=a_id).update(admin_name=name,admin_dob=dob,admin_email=email) 
          return redirect('admin1:profile_admin')
     else:
          data=Staff.objects.get(id=a_id) 
          return render(request,"admin1/edit_profile.html",{'data':data} )    

def get_dashboard(request):
     if 'admin_id' in request.session :
          return render(request,"admin1/dashboard.html")
          
     return render(request,"admin1/dashboard.html")

def logoutadmin(request):
     del request.session['admin_id']
     return redirect('admin1:admin1_home')

def profileadmin(request):
     if 'admin_id' in request.session:
          
          a_id=request.session['admin_id']
          admin_details=Staff.objects.get(id=a_id) 
        
          return render(request,"admin1/profile_admin.html",{ 'data': admin_details})
     else:
          return redirect('admin1:admin1_home')
     
def get_add_class(request):
     if request.method=='POST':
          class_name=request.POST.get('classname1') 
          class_sem=request.POST.get('sem') 
          classes=Class(class_name=class_name,class_sem=class_sem) 
          classes.save()
     clss=Main.objects.all()   
     return render(request,"admin1/add_class.html",{'class_details':clss}) 

def get_student_classes(request):
     cls=Main.objects.all()
     clss=Class.objects.all()
     return render(request,"admin1/student_classes.html",{'class_details':clss})

def get_delete_class(request,c_id):
    Class.objects.get(id=c_id).delete()
    return redirect('admin1:student_classes') 
   
def get_update_class(request,c_id):
     if request.method=='POST':
          class_name=request.POST['classname1']
          class_sem=request.POST.get('sem2') 
          Class.objects.filter(id=c_id).update(class_name=class_name,class_sem=class_sem) 
          return redirect('admin1:student_classes') 
     
     clss=Main.objects.all()   
     return render(request,"admin1/update_class.html",{'class_details':clss})

def get_view_class(request):
     clss=Class.objects.all()
     return render(request,"admin1/view_class.html",{'class_details':clss})

def get_view_subject(request,cl_id):
    
    subjects = Subject.objects.filter(class_id_id=cl_id)     
    return render(request, "admin1/view_subject.html", {'subjects': subjects})

def get_manage_sub(request):
     if request.method=='POST':
          id=request.POST['classid2']
          class_sub=request.POST['classsubject']
          class_subid=request.POST['classsubid']
          class_teacher=request.POST['classteacher']
          credit=request.POST['credit']
          subjects=Subject(class_id_id=id,class_sub=class_sub,class_subid=class_subid,class_teacher=class_teacher,credit=credit)  
          subjects.save()
     clss=Class.objects.all()   
     return render(request,"admin1/manage_sub.html",{'class_details':clss})

def get_delete_subject(request,s_id,class_id):
     Subject.objects.get(id=s_id).delete()
     return redirect('admin1:view_subject',cl_id=class_id)  
     
def get_notice(request):
     if request.method=='POST':
          class_notice=request.POST['inputnotice']
          notice=Notice(class_notice=class_notice)
          notice.save()
     return render(request,"admin1/notice.html")

def get_notice_list(request):   
     notice=Notice.objects.all()
     return render(request,"admin1/notice_list.html",{'notices':notice})

def get_manage_student(request):
     
     clss=Class.objects.all()
     return render(request,"admin1/manage_student.html",{'class_details':clss})  

def get_student_detail(request,cl_id):
     students=Student.objects.filter(student_sem=cl_id) 
     return render(request,"admin1/student_detail.html",{'students':students})

def checkusernameexist(request):
    roll=request.POST['stu_roll']
    user=Student.objects.filter(student_roll=roll).exists()
    if user :
        return JsonResponse({'is_available': False})
    else:
        return JsonResponse({'is_available':True})

def get_delete_student(request,c_id,class_id): 
     Student.objects.get(id=c_id).delete()
     return redirect('admin1:student_detail',cl_id=class_id) 

def get_edit_student(request,c_id,class_id):
     if request.method=='POST':
          s_name=request.POST['fullname']
          s_id=request.POST['rollid']
          s_email=request.POST['email']
          s_dob=request.POST['dob']
          s_gender=request.POST['gender']
          s_classid=request.POST['classid']  
          
          Student.objects.filter(id=c_id).update(student_name=s_name,student_roll=s_id,student_email=s_email,student_dob=s_dob,
                           student_gender=s_gender,student_sem_id=s_classid) 
          
          return redirect('admin1:student_detail', cl_id=class_id) 
             
     else:
          data=Student.objects.get(id=c_id) 
          clss=Class.objects.all()
          
     return render(request,"admin1/edit_student.html",{'class_details':clss,'data':data}) 

def get_add_student(request):
     message=""
     if request.method=="POST":
          s_name=request.POST['fullname']
          s_id=request.POST['rollid']
          s_email=request.POST['semail']
          s_dob=request.POST['dofb']
          s_gender=request.POST['gender']
          s_classid=request.POST['class']  
          s_semid=request.POST['semester'] 
          
          
          student_exist=Student.objects.filter(student_email=s_email).exists()
          if not student_exist :
               otp=randint(1000,9999)
               send_mail(
                    'Plaese verify your otp',
                    str(otp),
                    settings.EMAIL_HOST_USER,
                    [s_email], 
               )
               stu=Student(student_name=s_name,student_roll=s_id,student_email=s_email,student_dob=s_dob,
                           student_gender=s_gender,student_class=s_classid,student_sem_id=s_semid,student_password=str(otp),status='to_verify')  
               stu.save()
               student_data=Student.objects.get(student_email=s_email)
               request.session['student_id']=student_data.id
               
               return redirect('admin1:add_student') 
          else:
               message="student already exist"
     clss=Class.objects.all()          
     cls=Main.objects.all()
     return render(request,"admin1/add_student.html",{'class_details':clss,'class':cls})

def get_semester_by_class_name(request):
    class_name = request.GET.get('class_name')
    semesters = Class.objects.filter(class_name=class_name).values('id','class_sem') 

    return JsonResponse(list(semesters), safe=False)  

def get_view_attend(request):
     cls=Class.objects.all()
     return render(request,'admin1/view_attend.html',{'class_details':cls}) 

def get_view_attendance(request,cl_id):
     cls=Class.objects.get(id=cl_id)
     students=Student.objects.filter(student_sem=cl_id)
     month = Month.objects.all() 
     
     return render(request, 'admin1/view_attendance.html', {'students': students, 'cls': cls,'month':month})    
     
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

        return JsonResponse({'total_working_days': total_working_days,'month_id':selected_month}) 

def fetch_attendance_data(request):
    if request.method == 'GET':
        student_id = request.GET.get('student_id')
        class_id = request.GET.get('class_id')
        month = request.GET.get('month')

        # Fetch attendance data for the selected student, class, and month
        try:
            student = Student.objects.get(id=student_id)
            cls = Class.objects.get(id=class_id)
            attendance = Attendance.objects.get(student_id=student, class_id=cls, month=month)

            # Prepare the attendance data as a dictionary to be sent in the AJAX response
            attendance_data = {
                 'id': attendance.id,
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

            return JsonResponse(attendance_data)
        except (Student.DoesNotExist, Class.DoesNotExist, Attendance.DoesNotExist):
            return JsonResponse({'error': 'Attendance data not found.'})

    return JsonResponse({'error': 'Invalid request method.'})
  
def get_attendance(request):
    clss = Class.objects.all()
    month = Month.objects.all()
    students_list = []
    for cl in clss:
        students = Student.objects.filter(student_sem_id=cl.id)
        students_list.extend(students)
    return render(request, "admin1/attendance.html", {'class_details': clss, 'students': students_list,'month':month}) 

def save_attendance(request):
    if request.method == "POST": 
        class_id = request.POST.get('classid')
        student_id = int(request.POST.get('studentId'))
        month=int(request.POST.get('month')) 
        present = int(request.POST.get('present_field', 0))
        absent = int(request.POST.get('absent_field', 0))

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Invalid student ID.'})

        # Create or update the Attendance object
        attendance, created = Attendance.objects.update_or_create(
            class_id_id=class_id,
            student_id_id=student_id,
            month=month,
            defaults={
                'day1': int(request.POST.get('day1', 0)),
                'day2': int(request.POST.get('day2', 0)),
                'day3': int(request.POST.get('day3', 0)),
                'day4': int(request.POST.get('day4', 0)),
                'day5': int(request.POST.get('day5', 0)),
                'day6': int(request.POST.get('day6', 0)),
                'day7': int(request.POST.get('day7', 0)),
                'day8': int(request.POST.get('day8', 0)),
                'day9': int(request.POST.get('day9', 0)),
                'day10': int(request.POST.get('day10', 0)),
                'day11': int(request.POST.get('day11', 0)),
                'day12': int(request.POST.get('day12', 0)),
                'day13': int(request.POST.get('day13', 0)),
                'day14': int(request.POST.get('day14', 0)),
                'day15': int(request.POST.get('day15', 0)),
                'day16': int(request.POST.get('day16', 0)),
                'day17': int(request.POST.get('day17', 0)),
                'day18': int(request.POST.get('day18', 0)),
                'day19': int(request.POST.get('day19', 0)),
                'day20': int(request.POST.get('day20', 0)),
                'day21': int(request.POST.get('day21', 0)),
                'day22': int(request.POST.get('day22', 0)),
                'day23': int(request.POST.get('day23', 0)),
                'day24': int(request.POST.get('day24', 0)),
                'day25': int(request.POST.get('day25', 0)),
                'day26': int(request.POST.get('day26', 0)),
                'day27': int(request.POST.get('day27', 0)),
                'day28': int(request.POST.get('day28', 0)),
                'day29': int(request.POST.get('day29', 0)),
                'day30': int(request.POST.get('day30', 0)),
                'day31': int(request.POST.get('day31', 0)),
                
            }
        )

        return JsonResponse({'success': True, 'message': 'Data saved successfully.'})
     
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def get_students_by_class(request):
    class_id = request.GET.get('classid')
    students = Student.objects.filter(student_sem_id=class_id).values('id', 'student_roll', 'student_name')
    return JsonResponse(list(students), safe=False)

def get_edit_attendance(request,id):
     
     attend=Attendance.objects.get(id=id) 
     s_id=attend.student_id_id      
     if request.method=='POST':
          day1=request.POST.get('day1')
          day2=request.POST['day2']
          day3=request.POST['day3']
          day4=request.POST['day4']
          day5=request.POST['day5']
          day6=request.POST['day6']
          day7=request.POST['day7']
          day8=request.POST['day8']
          day9=request.POST['day9']
          day10=request.POST['day10']
          day11=request.POST['day11']
          day12=request.POST['day12']
          day13=request.POST['day13']
          day14=request.POST['day14']
          day15=request.POST['day15']
          day16=request.POST['day16']
          day17=request.POST['day17']
          day18=request.POST['day18']
          day19=request.POST['day19']
          day20=request.POST['day20']
          day21=request.POST['day21']
          day22=request.POST['day22']
          day23=request.POST['day23']
          day24=request.POST['day24']
          day25=request.POST['day25']
          day26=request.POST['day26']
          day27=request.POST['day27']
          day28=request.POST['day28']
          day29=request.POST['day29']
          day30=request.POST['day30']
          day31=request.POST['day31']
          
          c_id=attend.class_id_id
          
          Attendance.objects.filter(id=id).update(day1=day1,day2=day2,day3=day3,day4=day4,day5=day5,day6=day6,day7=day7,day8=day8,day9=day9,
          day10=day10,day11=day11,day12=day12,day13=day13,day14=day14,day15=day15,day16=day16,day17=day17,day18=day18,day19=day19,
          day20=day20,day21=day21,day22=day22,day23=day23,day24=day24,day25=day25,day26=day26,day27=day27,day28=day28,day29=day29,
          day30=day30,day31=day31) 
          return redirect('admin1:view_attendance' , c_id) 
     else:
          
          # students=Student.objects.get(id=student_id) 
          
          return render(request,"admin1/edit_attendance.html",{'attend':attend,'s_id':s_id})  

def get_fee(request):
     fee=Fee.objects.all()
          
     return render(request,"admin1/fee.html",{'fees':fee})

def get_edit_fee(request):
     if request.method=="POST":
          class_name=request.POST['inputclass7']
          tuition_fee=request.POST['inputtuition7']
          special1=request.POST['inputfee1']
          special2=request.POST['inputfee2']
          special3=request.POST['inputfee3']
          deposit_fee=request.POST['inputdeposit']
          sem1_fee=request.POST['inputsem1']         
          sem2_fee=request.POST['inputsem2'] 
          sem3_fee=request.POST['inputsem3']  
          sem4_fee=request.POST['inputsem4']  
          sem5_fee=request.POST['inputsem5']  
          sem6_fee=request.POST['inputsem6']   
          fees=Fee(class_name=class_name,tuition_fee=tuition_fee,special1=special1,special2=special2,special3=special3,
                   deposit_fee=deposit_fee,sem1_fee=sem1_fee,sem2_fee=sem2_fee,sem3_fee=sem3_fee,sem4_fee=sem4_fee,sem5_fee=sem5_fee,sem6_fee=sem6_fee)
          fees.save() 
     clss=Main.objects.all()   
     return render(request,"admin1/edit_fee.html",{'class_details':clss})

def get_update_fee(request,s_id):
     if request.method=='POST':
          
          tuition_fee=request.POST['inputtuition8']
          special1=request.POST['inputfee4']
          special2=request.POST['inputfee5'] 
          special3=request.POST['inputfee6']
          deposit_fee=request.POST['inputdeposit1']
          sem1_fee=request.POST['input1sem']         
          sem2_fee=request.POST['input2sem'] 
          sem3_fee=request.POST['input3sem']  
          sem4_fee=request.POST['input4sem']  
          sem5_fee=request.POST['input5sem']  
          sem6_fee=request.POST['input6sem']       
          Fee.objects.filter(id=s_id).update(tuition_fee=tuition_fee,special1=special1,special2=special2,special3=special3,
                   deposit_fee=deposit_fee,sem1_fee=sem1_fee,sem2_fee=sem2_fee,sem3_fee=sem3_fee,sem4_fee=sem4_fee,sem5_fee=sem5_fee,sem6_fee=sem6_fee) 
          return redirect('admin1:fee') 
     else:
          data=Fee.objects.get(id=s_id) 
          clss=Main.objects.all()   
          return render(request,"admin1/update_fee.html",{'class_details':clss,'data':data})  

def get_student_result(request): 
     cls=Class.objects.all()
     return render(request,"admin1/student_result.html",{'class_details':cls})

def get_view_result(request,c_id):
     cls=Class.objects.get(id=c_id) 
     sub=Subject.objects.filter(class_id=c_id)
     subject=request.GET.get('subjectid') 
     students=Student.objects.filter(student_sem=c_id)
     for s in students:
          result=Results.objects.filter(class_id=c_id,student_roll=s.id,sub_id=subject)
     return render(request,'admin1/view_result.html',{'subjects':sub,'students':students,'cls':cls,'result':result}) 


def get_mark_details(request):
    if request.method == 'GET':
        class_id = request.GET.get('classid')
        subject_id = request.GET.get('subjectid')
        student_id = request.GET.get('studentid')

        # Check if student_id, class_id, and subject_id are valid integers
        try:
            student_id = int(student_id)
            class_id = int(class_id)
            subject_id = int(subject_id)
        except (TypeError, ValueError):
            return JsonResponse({'error': 'Invalid student, class, or subject ID.'})

        try:
            student = Student.objects.get(id=student_id)
            cls = Class.objects.get(id=class_id)
            subject = Subject.objects.get(id=subject_id)
            result = Results.objects.get(class_id_id=cls, student_roll=student, sub_id=subject)

            result_data = {
                 'id':result.id,
                'result1': result.marks,
                'result2': result.total_marks,
                'result3': result.grade,
            }
            return JsonResponse(result_data)
        except (Student.DoesNotExist, Class.DoesNotExist, Subject.DoesNotExist, Results.DoesNotExist):
            return JsonResponse({'error': 'Result data not found.'})

    return JsonResponse({'error': 'Invalid request method.'})

def get_result(request):      
     clss = Class.objects.all()
     cls=Main.objects.all()
     
     for cl in clss:
          students=Student.objects.filter(student_sem_id= cl.id)       
     return render(request, 'admin1/result.html', {'class_details': clss,'students': students,'classes':cls})  

def get_edit_result(request, result_id):
    result = Results.objects.get(id=result_id)
    c_id=result.class_id_id
    if request.method == 'POST':
        mark = request.POST['inputMarks3']
        grade = request.POST['inputGrade']
        Results.objects.filter(id=result_id).update(marks=mark, grade=grade)
        return redirect('admin1:view_result',c_id) 
    else:
        data = Results.objects.get(id=result_id)  
        return render(request, "admin1/edit_result.html", {'data': data})


def save_results(request):
    if request.method == "POST":
        class_id = request.POST.get('classid')  # Use 'classid' to match the JavaScript key
        class_name = request.POST.get('classname')  # Use 'classname' to match the JavaScript key
        subject_id = request.POST.get('subjectid')
        student_id = request.POST.get('studentId')
        marks = request.POST.get('marks')
        grade = request.POST.get('grade')
        grade_point = request.POST.get('grade_point')  # Correct the key to match JavaScript
        
        try:
            class_obj = Class.objects.get(id=class_id)
        except Class.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Invalid class_id.'})
        
        # Create or update the Results object
        result, created = Results.objects.update_or_create(
            class_id=class_obj,
            sub_id_id=subject_id,
            student_roll_id=student_id,
            class_name=class_name,
            defaults={
                'marks': marks,
                'grade': grade,
                'total_marks': '100',
                'grade_point': grade_point,
            }
        )
        
        return JsonResponse({'success': True, 'message': 'Data saved successfully.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})

  
def get_semester_by_class_name(request):
    class_name = request.GET.get('class_name')
    classes = Class.objects.filter(class_name=class_name).values('id', 'class_sem') 
    return JsonResponse(list(classes), safe=False)

def get_students_by_semester(request):
    class_id = request.GET.get('semester') 
    students = Student.objects.filter(student_sem_id=class_id).values('id', 'student_name', 'student_roll')
    return JsonResponse(list(students), safe=False)

def get_subjects_by_semester(request):
    class_id = request.GET.get('semester_id') 
    subjects = Subject.objects.filter(class_id_id=class_id).values('id', 'class_sub')  
    return JsonResponse(list(subjects), safe=False) 
