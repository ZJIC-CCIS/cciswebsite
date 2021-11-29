from django.db import models


# Create your models here.

class Notice(models.Model):
    name = models.CharField(max_length=100, verbose_name="公告标题")
    content = models.TextField(verbose_name="公告内容")
    dates = models.CharField(max_length=30,verbose_name="日期")

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = '公告'
        db_table = 'all_notice'
