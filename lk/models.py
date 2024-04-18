from django.db import models
from django.contrib.auth.models import AbstractUser
from lk.const import *
from django.conf import settings

# Create your models here.
class User(AbstractUser):

    user_type = models.CharField(verbose_name='Должность', max_length=10, choices=USER_TYPE_CHOICES, default=USER_TYPE_EMPLOYEE)
    user_boss = models.ForeignKey('self', verbose_name='Начальник', on_delete=models.CASCADE, blank=True, null=True, default='')
    available_days = models.IntegerField( verbose_name='Дней отпуска', blank=True, null=True, default=28)
    is_14 = models.BooleanField(default=False)

    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    
    def __str__(self):
        return self.username