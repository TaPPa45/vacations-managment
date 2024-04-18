from django.db import models
from lk.models import User
from vacations.const import *

# Create your models here.
class VacationRequest(models.Model):    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField(verbose_name="Начало отпуска")
    finish_date = models.DateField(verbose_name="Конец отпуска")

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=WAITING,
    )
    days = models.IntegerField(verbose_name='количество дней', blank=True, null=True)
    comment = models.TextField(verbose_name='комментарий', blank=True, null=True)
    class Meta:
        verbose_name = 'Запрос на отпуск'

    def __str__(self):
        return f"Запрос на отпуск от {self.user.first_name} {self.user.last_name} на {self.days} дней, с {self.start_date} по {self.finish_date}"