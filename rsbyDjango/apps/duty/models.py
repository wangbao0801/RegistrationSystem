# -*- coding:utf-8 -*-
__author__ = 'evaseemefly'
__date__ = '2018/4/17 16:33'
from django.db import models
from datetime import datetime

# Create your models here.

class UserInfo(models.Model):
    uid=models.AutoField(primary_key=True)
    username=models.CharField(default='值班员',max_length=20)
    isdel=models.BooleanField(default=False)
    #注意不能使用default=datetime.now
    createdate=models.DateField(auto_now_add=True,null=True)
    modeificateddate=models.DateField(auto_now=True,null=True)

class DepartmentInfo(models.Model):
    parent_department_choices={
        (1, '数值室'),
        (2, '气象室'),
        (3, '环境室'),
        (4, '预警室')
    }
    did=models.AutoField(primary_key=True)
    pid=models.IntegerField(choices=parent_department_choices)
    derpartmentname=models.CharField(default='默认部门',max_length=20)

    class Meta:
        # 设置了此名称后在xadmin中可以显示该别名
        verbose_name="部门信息"
        verbose_name_plural=verbose_name

class DutyInfo(models.Model):
    duid=models.AutoField(primary_key=True)
    dutyname=models.CharField(default='主班',max_length=20)
    isdel=models.BooleanField(default=False)
    createdate=models.DateField(auto_now_add=True,null=True)
    modeificateddate=models.DateField(auto_now=True,null=True)

    class Meta:
        verbose_name="值班类别"
        verbose_name_plural=verbose_name

class dutyschedule(models.Model):
    id=models.AutoField(primary_key=True)
    dutydate=models.DateField(auto_now=True)

class R_UserInfo_DepartmentInfo(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    did=models.ForeignKey(DepartmentInfo,on_delete=models.CASCADE)

class R_DepartmentInfo_DutyInfo(models.Model):
    id=models.AutoField(primary_key=True)
    did=models.ForeignKey(DepartmentInfo,on_delete=models.CASCADE)
    duid=models.ForeignKey(DutyInfo,on_delete=models.CASCADE)