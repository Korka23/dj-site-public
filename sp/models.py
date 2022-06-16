from django.db import models

class SpLic(models.Model):
    id = models.AutoField(primary_key=True)
    fc_mo = models.CharField(max_length=8)
    name = models.CharField(max_length=255, blank=True, null=True)
    c_prof = models.IntegerField(blank=True, null=True)
    date_b = models.DateField()
    date_e = models.DateField(blank=True, null=True, default='01.01.2070')
    deleted = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sp_lic'
        ordering = ['fc_mo']

    def get_absolute_url(self):
        return f'/sp/{self.id}'

# Create your models here.
