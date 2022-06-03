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
    #def __str__(self):
        #return self.s

    def get_absolute_url(self):
        return f'/ksg/{self.id}'

    class Meta:
        db_table = 'ksg_p'
        ordering = ['id']


class dj_smj_c(models.Model):
    idd = models.ForeignKey(dj_ksg_p, on_delete=models.CASCADE, db_column='idd')
    name = models.CharField(max_length=100)
    c_prof = models.IntegerField()
    KSG = models.CharField(max_length=100)
    prof = ArrayField(
        models.IntegerField(blank=True, null=True),
        blank=True,
        null=True
    )
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'smj_c'
        ordering=['idd']


class Controls(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    c_prof = models.BigIntegerField(blank=True, null=True)
    ksg = models.CharField(db_column='KSG', max_length=8, blank=True, null=True)  # Field name made lowercase.
    array_agg = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'controls'

'''
class LicView(models.Model):
    id = models.IntegerField(db_column= 'id_prof', primary_key=True)
    id_mo = models.IntegerField(blank=True, null=True)
    fc_mo = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    c_prof = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'lic_view'
        ordering = ['id']


    def get_absolute_url(self):
        return f'/LicView/{self.id}'
        '''

class LicMain(models.Model):
    id_mo = models.AutoField(primary_key=True)
    fc_mo = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lic_main'

class LicDop(models.Model):
    id_prof = models.AutoField(primary_key=True)
    id_mo = models.ForeignKey('LicMain', models.DO_NOTHING, db_column='id_mo', blank=True, null=True)
    c_prof = models.IntegerField(blank=True, null=True)
    date_b = models.DateField(blank=True, null=True)
    date_e = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lic_dop'

class LicMash(models.Model):
    id_prof = models.AutoField(primary_key=True)
    fc_mo = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    c_prof = models.IntegerField()
    date_b = models.DateField(default='01.04.2022')
    date_e = models.DateField(default='30.04.2022')

    class Meta:
        managed = True
        ordering = ['fc_mo']
        db_table = 'lic_mash'

    def get_absolute_url(self):
        return f'/LicView/{self.id_prof}'



