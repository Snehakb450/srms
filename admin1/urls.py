from django.urls import path
from . import views
app_name='admin1'

urlpatterns = [
    path ('admin_master/',views.get_admin_master, name="admin_master"),
    
    path ('admin1_home/',views.get_admin1_home, name="admin1_home"),
    
    path ('register/',views.get_register, name="register"),
    
    path('dashboard/',views.get_dashboard, name="dashboard"),
    
    path('logout_admin', views.logoutadmin,name="logout_admin"),
    
    path('profile_admin/', views.profileadmin,name="profile_admin"),
    path('edit_profile/<int:a_id>',views.get_edit_profile, name="edit_profile"), 
    
    path ('admin1_forgot/',views.get_admin1_forgot, name="admin1_forgot"),
   
    
    path ('student_classes/',views.get_student_classes, name="student_classes"),
    path('add_class/',views.get_add_class, name="add_class"),
    path('delete_class/<int:c_id>',views.get_delete_class, name="delete_class"),
    path('update_class/<int:c_id>',views.get_update_class, name="update_class"),
    
    path('manage_student/',views.get_manage_student, name="manage_student"),
    path('student_detail/<int:cl_id>',views.get_student_detail, name="student_detail"),
    path('edit_student/<int:c_id>/<int:class_id>',views.get_edit_student, name="edit_student"),
    path('add_student/',views.get_add_student,name="add_student"),
    path('delete_student/<int:c_id>/<int:class_id>',views.get_delete_student, name="delete_student"),
    path('checkusername/',views.checkusernameexist, name="checkusername"),
    path('get_semester_by_class_name/', views.get_semester_by_class_name, name='get_semester_by_class_name'),
   
    path('view_class/',views.get_view_class, name="view_class"),
    path('view_subject/<int:cl_id>', views.get_view_subject, name='view_subject'), 
    path('manage_sub/',views.get_manage_sub, name="manage_sub"),
    path('delete_subject/<int:s_id>/<int:class_id>',views.get_delete_subject, name="delete_subject"),

    path('notice/',views.get_notice, name="notice"),
    path('notice_list/',views.get_notice_list, name="notice_list"),
    
    path('attendance/',views.get_attendance, name="attendance"),
    path('save_attendance/',views.save_attendance,name="save_attendance"), 
    path('view_attend/',views.get_view_attend,name="view_attend"),
    path('view_attendance/edit_attendance/<int:id>', views.get_edit_attendance, name='edit_attendance'),
    path('view_attendance/<int:cl_id>',views.get_view_attendance,name="view_attendance"), 
    path('fetch_attendance/', views.fetch_attendance_data, name='fetch_attendance'),
    path('get_students/', views.get_students_by_class, name='get_students_by_class'),
    path('fetch_total/', views.fetch_total, name='fetch_total'),
    
    
    path('change/',views.get_change, name="change"),  
    
    path('fee/',views.get_fee, name="fee"),
    path('edit_fee/',views.get_edit_fee, name="edit_fee"),
    path('update_fee/<int:s_id>',views.get_update_fee, name="update_fee"), 
    
    path('result/',views.get_result, name="result"),
    path('student_result/',views.get_student_result, name="student_result"),
    path('save_results/', views.save_results, name="save_results"),
    path('view_result/<int:c_id>',views.get_view_result,name="view_result") ,
    path('view_result/edit_result/<int:result_id>',views.get_edit_result, name="edit_result") ,
    path('get_mark_details/', views.get_mark_details, name='get_mark_details') ,
    path('get_subjects_by_semester/', views.get_subjects_by_semester, name='get_subjects_by_semester'),
    path('get_students_by_semester/', views.get_students_by_semester, name='get_students_by_semester'),


]