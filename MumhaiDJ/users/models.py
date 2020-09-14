from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

    

class Customer(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, default="User First Name")
    last_name = models.CharField(max_length=25)
    user_type_choices = [
        ('C','Customer'),
        ('E','Employee'),
    ]
    user_type = models.CharField(
        max_length=1,
        choices = user_type_choices,
        default = 'C',
    )
    number = models.CharField(max_length=10)
    #dob = models.DateField(verbose_name='Date Of Birth')
    gender_choices = [
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]
    gender = models.CharField(
        max_length = 1,
        choices = gender_choices,
        default = 'M',
    )
    econ_name = models.CharField(verbose_name='Emergency Contact Name', max_length=25, blank=True, null=True)
    econ_num = models.CharField(verbose_name='Emergency Contact Number', max_length=10, blank=True, null=True)
    status_choices = [
        ('FR','Free'),
        ('BK','Booked'),
        ('PP','Payment Pending'),
    ]
    status = models.CharField(
        max_length = 2,
        choices = status_choices,
        default = 'FR',
    )
    
    
    def __str__(self):
        return self.first_name+" "+self.last_name;
    
    def getAnEmployee():
        return Customer.objects.filter(user_type='E').order_by('?')[0]
    
# Create your models here.
