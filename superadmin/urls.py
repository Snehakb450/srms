from django.urls import path
from . import views
app_name='superadmin'

urlpatterns = [
    path ('add_admin/',views.get_add_admin, name="add_admin"),
    path('dash/',views.get_dash,name="dash"),
    path('class/',views.get_class,name="class"),
    path('subjects/<int:cl_id>',views.get_subjects,name="subjects"),
    path('students/<int:cl_id>',views.get_students,name="students"),
    path('fees/',views.get_fees,name="fees"),
    path('notices/',views.get_notices,name="notices"), 
    path('logout_superadmin', views.logout_superadmin,name="logout_superadmin"),
    path ('',views.get_home, name="home"),
    path ('login/',views.get_login, name="login"),  
    path('change_password/',views.get_change_password, name="change_password") ,
    path('delete_admin/<int:a_id>',views.delete_admin,name="delete_admin"),
    path('update_admin/<int:a_id>',views.update_admin,name="update_admin") ,
    path('update_admin_status/', views.update_admin_status, name='update_admin_status'),
]