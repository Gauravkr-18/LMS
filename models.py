from django.db import models

userTypeData = (
    ("Teacher", "Teacher"),
    ("Student", "Student")
)
# Create your models here.
class lmsUser(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10 , null=True, blank=True)
    number = models.IntegerField(max_length=20, unique=True)  
    password = models.CharField(max_length=20)
    userType = models.CharField(max_length=10, choices=userTypeData)

    def __str__(self):
        return self.userName

class CourseUpload(models.Model):  
    courseUploadId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=20)
    courseDescription = models.CharField(max_length=50) 
    createdAt = models.DateField() 
    coursePlayList = models.CharField(max_length=10)
    courseDuration = models.CharField(max_length=10)  
    user = models.ForeignKey(lmsUser, on_delete=models.CASCADE)  

    def __str__(self):
        return self.courseName
