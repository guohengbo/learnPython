一、安装
1.pip install django后，使用django-admin startproject [filename]
    例如：E:\LearnPython\web>django-admin startproject myproject

2.生成的项目文件解析：
(1) manage.py：一个命令行工具，可以使你用多种方式对Django项目进行交互。 你可以在django-admin和manage.py中读到关于manage.py的所有细节。
(2) 内层的myproject/目录是你的项目的真正的Python包。它是你导入任何东西时将需要使用的Python包的名字（例如 myproject.urls）
(3)myproject/__init__.py：一个空文件，它告诉Python这个目录应该被看做一个Python包。
(4)myproject/settings.py：该Django 项目的设置/配置。Django 设置 将告诉你这些设置如何工作。
(5)myproject/urls.py：该Django项目的URL声明；你的Django站点的“目录”。 你可以在URL 转发器 中阅读到更多关于URL的内容。
(6)myproject/wsgi.py：用于你的项目的与WSGI兼容的Web服务器入口。 更多细节请参见如何利用WSGI进行部署。 

二、创建应用Polls
1.cd命令进入manage.py文件所在的目录，输入 python manage.py startapp polls
2.增加myproject中setting.py的install_app的"polls"与"bootstrap3"，否则不识别
3.在models.py中创建模型
```py
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
```
4.生成数据库表(自带sqlite,但真正项目时还是需要用到mysql等等)
    使用python manage.py makemigrations polls 命令生成
5.与数据库同步 python manage.py migrate
6.下载sqlite客户端，导入项目
7.修改admin.py
```py
from .models import Question,Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ] 
inlines = [ChoiceInline]
list_display = ('question_text', 'pub_date')


admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
```
8.创建用户名密码 python manage.py createsuperuser
    (momo wdfmo1995103)
9.启动服务 python manage.py runserver 
     127.0.0.1:8000/admin后台

三、定义视图
1.复制templates模板，主要是修改index.html
2.在urls.py里定义app_name='app名字'
视图要在views.py填写，并在urls.py里设置