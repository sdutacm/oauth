from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userid = models.IntegerField()
    user_name = models.CharField(max_length=256)
    nick_name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)


class UserPriv(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    tel = models.CharField(max_length=32)
    birthday = models.DateField()


class UserEdu(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    student_no = models.CharField(max_length=256)
    school = models.CharField(max_length=256)
    college = models.CharField(max_length=256)
    major = models.CharField(max_length=256)
    grade = models.CharField(max_length=256)
    clazz = models.CharField(max_length=256)


class UserSocial(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    site = models.CharField(max_length=256)
