from django.db import models


class BaseManager(models.Manager):
    pass


class Base(models.Model):
    name = models.CharField(max_length=150, null=True)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    objects = BaseManager()

    class Meta:
        db_table = "base"
