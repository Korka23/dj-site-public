from django.db import models

class SzpLic(models.Model):
    id = models.AutoField(primary_key=True)
    fc_mo = models.CharField(max_length=8)
    name = models.CharField(max_length=255, blank=True, null=True)
    c_prof = models.IntegerField(blank=True, null=True)
    date_b = models.DateField(blank=True, null=True, default='01.04.2022')
    date_e = models.DateField(blank=True, null=True, default='30.04.2022')

    class Meta:
        managed = False
        db_table = 'szp_lic'
        #ordering = ['fc_mo']
        ordering = ['fc_mo']

    def get_absolute_url(self):
        return f'/szp/{self.id}'

# Create your models here.