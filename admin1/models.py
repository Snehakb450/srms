from django.db import models

# Create your models here.
class Staff(models.Model):
    admin_name=models.TextField(max_length=20,db_column="ad_name")
    admin_id=models.TextField(max_length=10,db_column="ad_id")
    admin_dob=models.DateField(db_column="ad_dob")
    admin_gender=models.TextField(max_length=20,db_column="ad_gender")
    admin_email=models.TextField(max_length=30,db_column="ad_email")
    admin_password=models.TextField(max_length=20,db_column="ad_password",null=True)
    status=models.TextField(max_length=20,db_column="status",default="to_approve",null=True) 
    
    class Meta:
        db_table="staff"
        
class Main(models.Model):
    class_name=models.TextField(max_length=20,db_column="class")
    
    class Meta:
        db_table="main"
        
class Class(models.Model):
    class_name=models.TextField(max_length=20,db_column="class_name",null=True)
    class_sem=models.TextField(max_length=20,db_column="class_sem")
    
    class Meta:
        db_table="classes"
        
class Notice(models.Model):
    class_notice=models.TextField(max_length=200,db_column="class_notice")
    
    class Meta:
        db_table="notices"
        
class Fee(models.Model):
    class_name=models.TextField(max_length=20,db_column="class_name")
    tuition_fee=models.TextField(max_length=10,db_column="tuition_fee",null=True)
    special1=models.TextField(max_length=10,db_column="special_fee1",null=True)
    special2=models.TextField(max_length=10,db_column="special_fee2",null=True)
    special3=models.TextField(max_length=10,db_column="special_fee3",null=True)
    deposit_fee=models.TextField(max_length=10,db_column="deposit",null=True)
    sem1_fee=models.TextField(max_length=10,db_column="sem_fee1",null=True)
    sem2_fee=models.TextField(max_length=10,db_column="sem_fee2",null=True)
    sem3_fee=models.TextField(max_length=10,db_column="sem_fee3",null=True)
    sem4_fee=models.TextField(max_length=10,db_column="sem_fee4",null=True)
    sem5_fee=models.TextField(max_length=10,db_column="sem_fee5",null=True)
    sem6_fee=models.TextField(max_length=10,db_column="sem_fee6",null=True)
    
    class Meta:
        db_table="fees"
  
class Student(models.Model):
    student_name=models.TextField(max_length=20,db_column="stu_name")
    student_roll=models.TextField(max_length=20,db_column="stu_roll")
    student_email=models.TextField(max_length=30,db_column="stu_email")
    student_gender=models.TextField(max_length=20,db_column="stu_gender")
    student_dob=models.DateField(db_column="stu_dob")
    student_class=models.TextField(max_length=20,db_column="student_class",null=True) 
    student_sem=models.ForeignKey(Class,on_delete=models.CASCADE,null=True) 
    student_password=models.TextField(max_length=30,db_column="stu_password")
    otp=models.TextField(max_length=10,db_column="otp",null=True)
    status=models.TextField(max_length=50,db_column="status",default="",null=True)
    
    class Meta:
        db_table="student"
          
class Subject(models.Model):
    class_id=models.ForeignKey(Class,on_delete=models.CASCADE,null=True) 
    class_sub=models.TextField(max_length=20,db_column="sub_name")
    class_subid=models.TextField(max_length=20,db_column="sub_id")
    class_teacher=models.TextField(max_length=20,db_column="teacher_name")
    credit=models.IntegerField(db_column="credit",default=1)  
    
    class Meta:
        db_table="subjects"
  
class Results(models.Model):
        class_id=models.ForeignKey(Class,on_delete=models.CASCADE,null=True) 
        class_name=models.TextField(max_length=20,db_column="class_name",null=True)
        sub_id=models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
        student_roll=models.ForeignKey(Student,on_delete=models.CASCADE,null=True) 
        marks=models.TextField(max_length=10,db_column="marks",default=100)
        total_marks=models.TextField(max_length=10,db_column="total_marks",default=0)
        grade=models.TextField(max_length=5,db_column="grade",default="")
        grade_point=models.IntegerField(db_column="grade_point",default=1)
    
        class Meta:
            db_table="results"
            
                  
class Attendance(models.Model): 
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, null=True) 
    month=models.IntegerField(db_column="month",null=True) 
    day1=models.IntegerField(db_column="day1",default=0)
    day2=models.IntegerField(db_column="day2",default=0)
    day3=models.IntegerField(db_column="day3",default=0)
    day4=models.IntegerField(db_column="day4",default=0)
    day5=models.IntegerField(db_column="day5",default=0)
    day6=models.IntegerField(db_column="day6",default=0)
    day7=models.IntegerField(db_column="day7",default=0)
    day8=models.IntegerField(db_column="day8",default=0)
    day9=models.IntegerField(db_column="day9",default=0)
    day10=models.IntegerField(db_column="day10",default=0)
    day11=models.IntegerField(db_column="day11",default=0)
    day12=models.IntegerField(db_column="day12",default=0)
    day13=models.IntegerField(db_column="day13",default=0)
    day14=models.IntegerField(db_column="day14",default=0)
    day15=models.IntegerField(db_column="day15",default=0)
    day16=models.IntegerField(db_column="day16",default=0)
    day17=models.IntegerField(db_column="day17",default=0) 
    day18=models.IntegerField(db_column="day18",default=0)
    day19=models.IntegerField(db_column="day19",default=0)
    day20=models.IntegerField(db_column="day20",default=0)
    day21=models.IntegerField(db_column="day21",default=0)
    day22=models.IntegerField(db_column="day22",default=0)
    day23=models.IntegerField(db_column="day23",default=0)
    day24=models.IntegerField(db_column="day24",default=0)
    day25=models.IntegerField(db_column="day25",default=0)
    day26=models.IntegerField(db_column="day26",default=0)
    day27=models.IntegerField(db_column="day27",default=0)
    day28=models.IntegerField(db_column="day28",default=0)
    day29=models.IntegerField(db_column="day29",default=0)
    day30=models.IntegerField(db_column="day30",default=0)
    day31=models.IntegerField(db_column="day31",default=0)
    
    class Meta:
        db_table="attendance"          

    
class Month(models.Model):
    month=models.CharField(max_length=20,db_column="month")
    total=models.IntegerField(db_column="total")
    
    class Meta:
        db_table="month"
        
        
    
