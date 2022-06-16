from django.db import models

class LicAppNew(models.Model):
    id_prof = models.AutoField(primary_key=True, serialize=True)
    fc_mo = models.CharField(max_length=8)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_b = models.DateField(blank=True, null=True, default='01.04.2022')
    idpr = models.IntegerField(blank=True, null=True)
    disp = models.CharField(max_length=10, blank=True, null=True)
    date_e = models.DateField(blank=True, null=True, default='01.01.2070')
    lic_num = models.CharField(max_length=255, blank=True, null=True)
    c_serv = models.IntegerField(blank=True, null=True)
    deleted = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lic_app_new'
        #ordering = ['fc_mo']
        ordering = ['fc_mo']

    def get_absolute_url(self):
        return f'/app/{self.id_prof}'
