from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    otp = models.IntegerField(default=456)
    role = models.CharField(max_length=30)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.email

class AdminUser(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    contactno = models.CharField(max_length=15)
    pic = models.FileField(upload_to="media/images/",default="media/admin.png")

    def __str__(self):
        return self.username+" ("+self.user_id.email+")"

class learners(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    contactno = models.CharField(max_length=15)
    city = models.CharField(max_length=60,blank=True,null=True)
    gender = models.CharField(max_length=10,blank=True,null=True)
    qualification = models.CharField(max_length=30,blank=True,null=True)
    primary_language = models.CharField(max_length=30,blank=True,null=True)
    status = models.BooleanField(default=False)
    pic = models.FileField(upload_to="media/images/",default="media/boy.png")

    # to diaplay profile pic as per their gender.
    def save(self, *args, **kwargs):
        if not self.pic or self.pic == "media/boy.png":  # Default image logic
            if self.gender == "Female":
                self.pic = "media/girl.png"
            else:
                self.pic = "media/boy.png"
        super().save(*args, **kwargs)  # Save to the database

    def __str__(self):
        return self.username+" ("+self.user_id.email+")"

class category(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category_name = models.CharField(max_length=30)
    category_pic = models.FileField(upload_to="media/images/",default="media/category.png")

class Course(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category_id = models.ForeignKey(category,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=60)
    fees = models.CharField(max_length=16)
    course_description = models.TextField()
    course_lecture_flow  = models.FileField(upload_to="media/lectureFLow/")
    course_handbook = models.FileField(upload_to="media/handbook/")
    course_interview_questions = models.FileField(upload_to="media/InterviewPreperation/")
    coure_assignments = models.FileField(upload_to="media/CourseAssignment/")
    coure_pic = models.FileField(upload_to="media/images/",default="media/course_pic.png")
    course_tutor_name = models.CharField(max_length=60)
    video_url = models.URLField(max_length=500, blank=True, null=True)
    quiz_url = models.URLField(max_length=500, blank=True, null=True)  # For quiz/exam links


    def __str__(self):
        return self.course_name
    
class company(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    company_name = models.CharField(max_length=255, unique=True)
    company_logo = models.FileField(upload_to="media/company_logos/", default="media/company_pic.png")
    company_description = models.TextField()
    company_website = models.URLField(blank=True, null=True,default="https://www.learnvern.com/")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name
    
class add_enroll_course(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    learners_id = models.ForeignKey(learners, on_delete=models.CASCADE) 
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)  
    created_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=30,default="PENDING")
    fees_status = models.CharField(max_length=20)
    paid_fees = models.IntegerField(default=0)

