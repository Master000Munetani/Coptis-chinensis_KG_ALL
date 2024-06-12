from django.db import models
# Create your models here.


class MyNode(models.Model):
    name = models.CharField(verbose_name='node的name', blank=True, null=True, default='', max_length=100)
    leixing = models.CharField(verbose_name='类型的中文', blank=True, null=True, default='', max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-id']
        verbose_name = '节点信息'
        verbose_name_plural = verbose_name
