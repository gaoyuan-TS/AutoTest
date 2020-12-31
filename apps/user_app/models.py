# -*- coding=utf-8 -*-
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('姓名', max_length=20,null=False)
    password = models.CharField('密码', max_length=20,null=False,default="123456")
    mobile = models.CharField('联系方式', max_length=20,null=False)
    email = models.CharField('邮箱', max_length=20,null=False)
    sex = models.IntegerField('性别', default=0)
    is_delete = models.IntegerField('是否删除',default=0)
    creat_time = models.DateTimeField('创建时间',auto_now_add=True)

    class Meta:
        db_table = 'user'
        verbose_name_plural = '用户信息'
        unique_together = ('mobile',)
