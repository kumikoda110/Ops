from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    login_status_ = (
        (0, '在线'),
        (1, '离线'),
        (2, '忙碌'),
        (3, '离开'),
    )
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', default='images/default.png', max_length=100)
    login_status = models.SmallIntegerField(choices=login_status_, default=1, verbose_name='登录状态')

    class Meta:
        db_table = 'ops_user'
        verbose_name = '用户表'
        verbose_name_plural = '用户表'


class UserLog(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='操作用户')
    remote_ip = models.GenericIPAddressField(verbose_name='操作用户IP')
    content = models.CharField(max_length=100, verbose_name='操作内容')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='操作时间')

    class Meta:
        db_table = 'ops_users_log'
        verbose_name = '用户管理操作记录表'
        verbose_name_plural = '用户管理操作记录表'
