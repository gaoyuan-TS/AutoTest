from django.db import models
from user_app.models import UserInfo


# Create your models here.
class TestCase(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('user_app.UserInfo', on_delete=models.CASCADE)
    test_name = models.CharField('测试用例名称', max_length=20,null=False)
    test_type=models.IntegerField('用例类型',default=0)
    is_delete = models.IntegerField('是否删除',default=0)
    creat_time = models.DateTimeField('创建时间',auto_now_add=True)


    class Meta:
        db_table = 'test_case'
        verbose_name_plural = '测试用例'
