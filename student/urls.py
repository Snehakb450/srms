from django.urls import path
from . import views
app_name='student'





urlpatterns = [ 
    path ('student_home/',views.get_student_home, name="student_home"),
    path ('student_dash/',views.get_student_dash, name="student_dash"),
    path ('student_forgot/',views.get_student_forgot, name="student_forgot"),
   
    path ('student_master/',views.get_student_master, name="student_master"),
    
    path('notices/',views.get_notices, name="notices"),
    
    path('change_pwd/',views.get_change_pwd, name="change_pwd"),
    
    path('attend/',views.get_attend, name="attend"), 
    path('fetch_attendance/', views.fetch_attendance, name='fetch_attendance'),
    
    path('results/',views.get_results, name="results"),
    path('fetch_subjects_and_results/', views.fetch_subjects_and_results, name='fetch_subjects_and_results'),
    path('pdf/<int:c_id>',views.pdf,name="pdf"),  
    # path('results_pdf/', views.generate_pdf, name='results_pdf'),
    # path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    #  path('generate-pdf/', GeneratePDFView.as_view(), name='generate_pdf'),
    
    path('fees/',views.get_fees, name="fees"),
    
    path('verify_otp/',views.get_verify_otp, name="verify_otp"),
    
    path('logout_student', views.logoutstudent,name="logout_student")
]



