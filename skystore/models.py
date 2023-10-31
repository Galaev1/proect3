from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100,verbose_name='имя')
    last_name = models.CharField(max_length=100,verbose_name='фамилия')
    avatar = models.ImageField(upload_to='students/',verbose_name='аватар',null=True,blank=True)
    is_active = models.BooleanField(default=True,verbose_name='good')
    def __str__(self):
        return f'{self.first_name},{self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'