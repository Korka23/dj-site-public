from django.db import models
from cleb import settings
import psycopg2
from psycopg2 import Error
from django.db import connection
from django.contrib.postgres.fields import ArrayField


class dj_ksg_p(models.Model):
    id = models.AutoField(primary_key=True,  unique=True, serialize=True)
    name = models.TextField()
    c_prof = models.IntegerField()
    smj_prof = ArrayField(
        models.IntegerField(blank=True, null=True),
        blank=True,
        null=True
    )
    KSG = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False, blank=True, null=True)
    date_b = models.DateField(blank=True, null=True)
    date_e = models.DateField(blank=True, null=True)
    #def __str__(self):
        #return self.s

    def get_absolute_url(self):
        return f'/ksg/{self.id}'

    class Meta:
        db_table = 'ksg_p'
        ordering = ['c_prof']






