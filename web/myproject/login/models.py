from django.db import models

# Create your models here.
#登录是一对一关系
#user(id,userName,passWord,pub_date)
class User(models.Model):
    userName=models.CharField(max_length=10)
    passWord=models.CharField(max_length=200)
    pub_date=models.DateTimeField()

    def __str__(self):
        return self.userName
 
