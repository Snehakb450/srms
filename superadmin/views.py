from django.shortcuts import render,redirect
from superadmin.models import Data
from admin1.models import Staff ,Class,Student,Subject,Fee,Notice
from django.http import JsonResponse
# Create your views here.
def get_home(request):
     return render(request,"superadmin/home.html") 

def get_login(request):
     if request.method=='POST':
          username=request.POST['username']
          password=request.POST['password'] 
          
          try:
               superadmin=Data.objects.get(username=username,password=password)
               request.session['superadmin_id']=superadmin.id 
               return redirect('superadmin:dash')
          except Data.DoesNotExist:
               return render(request,"superadmin/login.html",{'message':'Login failed'})
          
     
     return render(request,"superadmin/login.html") 


def get_add_admin(request):
     staffs=Staff.objects.all()         
     return render(request,"superadmin/add_admin.html",{'staffs':staffs}) 

def get_dash(request):
     total_classes = Class.objects.count()
     total_students = Student.objects.count()
     total_notices = Notice.objects.count()
     total_fees = Fee.objects.count()
     
     return render (request,'superadmin/dash.html', {
        'total_classes': total_classes,
        'total_students': total_students,
        'total_notices': total_notices,
        'total_fees': total_fees,
    })  

def get_class(request):
     data=Class.objects.all()
     return render (request,'superadmin/class.html',{'data':data})   

def get_students(request,cl_id): 
     students=Student.objects.filter(student_sem_id=cl_id)
     return render (request,'superadmin/students.html',{'students':students})  

def get_subjects(request,cl_id): 
     subjects = Subject.objects.filter(class_id_id=cl_id)    
     return render (request,'superadmin/subjects.html',{'subjects':subjects})   

def get_fees(request):
     fees=Fee.objects.all()
     return render (request,'superadmin/fees.html',{'fees':fees} )  

def get_notices(request):
     notice=Notice.objects.all()
     return render (request,'superadmin/notices.html',{'notices':notice})  

 
def update_admin_status(request):
    if request.method == 'POST':
        admin_id = request.POST.get('adminId')
        status = request.POST.get('status')
        
        # Assuming you have a model called 'Staff' with a field 'status' to store the admin status
        try:
            staff = Staff.objects.get(id=admin_id)
            staff.status = status
            staff.save()
            return JsonResponse({'success': True})
        except Staff.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Admin not found'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def logout_superadmin(request):
     del request.session['superadmin_id']
     return redirect('superadmin:login')

def get_change_password(request):
     if request.method=='POST':       
          current_pwd=request.POST['pwd9']
          new_pwd=request.POST['pwd10']
          super_id=request.session['superadmin_id']  
          data=Data.objects.get(id=super_id)
          if current_pwd==data.password :
               Data.objects.filter(id=super_id).update(password=new_pwd)
               return redirect('superadmin:add_admin')
         
     return render(request,"superadmin/change_password.html")

def delete_admin(request,a_id):
     Staff.objects.get(id=a_id).delete()
     return redirect('superadmin:add_admin') 

def update_admin(request,a_id):   
     Staff.objects.filter(id=a_id).update(status="Active") 
     return redirect ('superadmin:add_admin') 