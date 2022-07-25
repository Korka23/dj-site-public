from django.db import models

class Szp1Lic(models.Model):
    id = models.AutoField(primary_key=True)
    fc_mo = models.CharField(max_length=8)
    name = models.CharField(max_length=255, blank=True, null=True)
    c_prof = models.IntegerField(blank=True, null=True)
    date_b = models.DateField()
    date_e = models.DateField(blank=True, null=True, default='01.01.2070')
    deleted = models.BooleanField(blank=True, null=True, default=False)
    idpr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'szp1_lic'
        #ordering = ['fc_mo']
        ordering = ['fc_mo','c_prof']

    def get_absolute_url(self):
        return f'/szp1/{self.id}'

# Create your models here.
