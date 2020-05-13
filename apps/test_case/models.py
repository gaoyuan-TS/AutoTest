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


class TestCaseRunnerDetail(models.Model):
    id = models.AutoField(primary_key=True)
    test_case = models.ForeignKey('test_case.TestCase', on_delete=models.CASCADE)
    ip = models.CharField('测试地址', max_length=100,null=False)
    browser=models.CharField('浏览器',max_length=10,null=False)
    Version=models.CharField('版本', max_length=10,default="")
    report_address = models.CharField('测试用例地址', max_length=100, null=False)
    loop = models.IntegerField('循环次数',default=1)
    importAddress = models.CharField('测试报告地址',max_length=100, )
    moudle = models.CharField('运行的模块', max_length=15, default="全部")
    runner_time = models.DateTimeField('运行时间',auto_now_add=True)


    class Meta:
        db_table = 'testcase_runner_detail'
        verbose_name_plural = '测试用例运行详情'