from django.db import models
from django.utils import timezone
# Create your models here.
class Categorystay(models.Model):
    name = models.CharField(max_length=100, null = True, blank = True)
    def __str__(self):
        return self.name
    #tells django how our physical db will look like in the db
     

class Baby(models.Model):
    c_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True, blank = True)
    b_name = models.CharField(max_length=50, null = True, blank = True)
    age = models.IntegerField(null=True, blank = True, default=0)
    gender = models.CharField(max_length=50, null = True, blank=True)
    location = models.CharField(max_length=50, null = True, blank=True)
    sponsor = models.CharField(max_length=50, null = True, blank=True)
    timein = models.DateTimeField(null = True, blank=True)
    timeout = models.DateTimeField(null = True, blank=True)
    
    def __str__(self):
        return self.b_name
    
class Payment(models.Model):
        payee = models.ForeignKey(Baby, on_delete = models.CASCADE, null=True, blank = True)
        c_pay = models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True, blank = True)
        pay_no = models.IntegerField(null=True, blank=True, default=0)
        amount = models.IntegerField(null=True, blank=True, default=0)
        currency = models.CharField(max_length=10, default='ugx', null=True)
        
        def __int__(self):
            return self.currency
    