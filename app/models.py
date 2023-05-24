from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
from datetime import timedelta

class Staff(models.Model):
  # user = models.CharField(CustomUser, verbose_name='スタッフ', on_delete=models.CASCADE)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='スタッフ')

  def __str__(self):
    return str(self.user)

class Booking(models.Model):
  staff = models.ForeignKey(Staff, verbose_name='スタッフ', on_delete=models.CASCADE)
  first_name = models.CharField('性', max_length=100, null=True, blank=True)
  last_name = models.CharField('名', max_length=100, null=True, blank=True)
  tel = models.CharField('電話番号', max_length=100, null=True, blank=True)
  remarks = models.TextField('備考', default="", blank=True)
  start = models.DateTimeField('開始時間', default=timedelta(days=1))
  end = models.DateTimeField('終了時間', default=timedelta(days=1))

  def __str__(self):
    start = timezone.localtime(self.start).strtime('%Y/%m/%d %H:%M')
    end = timezone.localtime(self.end).strftime('%Y/%m/%d %H:%M')
    return f'{self.first_name}{self.last_name} {start} ~ {end} {self.staff}'