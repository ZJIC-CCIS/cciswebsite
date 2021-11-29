from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.
class Course(models.Model):
    picture = models.ImageField(upload_to='uploads/image/%Y/%m/%d', verbose_name='封面', null=True)
    name = models.CharField(max_length=100,verbose_name="授课标题")
    teacher = models.CharField(max_length=20, verbose_name="授课者姓名")
    classes = models.CharField(max_length=100, verbose_name="培训内容分类")
    content = MDTextField(verbose_name='文章内容')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'
        db_table = 'all_course'