from django.db import models

# Create your models here.
#使用manage.py生成时，会自动建立id为主键
#投票是一对多关系，外键放在多的那边
#问题表
class Question(models.Model):
    question_text=models.CharField(max_length=500)
    pub_date=models.DateTimeField()

    def __str__(self):
        return self.question_text

#选项
class Choice(models.Model):
    choice_text = models.CharField(max_length=500)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

#用户表
class User(models.Model):
    userName=models.CharField(max_length=200)
    passWord=models.CharField(max_length=100)
    email=models.EmailField()
    
    def __str__(self):
        return self.userName
