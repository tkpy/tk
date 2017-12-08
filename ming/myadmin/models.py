from django.db import models

# Create your models here.
# 姓名
class Name(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        db_table = 'name'  #更改表名

class Stuname(models.Model):
    name = models.CharField(max_length=15)
    status = models.IntegerField(default=1)
    date = models.CharField(max_length=20)

    class Meta:
        db_table = 'stuname' # 更改表名