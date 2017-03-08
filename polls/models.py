from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField(verbose_name="游戏名称", max_length=32)
    code = models.IntegerField(verbose_name="平台码", unique=True)
    coef = models.PositiveIntegerField(verbose_name='价格(单位:分)', default=0)

    class Meta:
        verbose_name = '游戏平台'
        verbose_name_plural = '游戏平台'

    def __str__(self):
        return self.name
