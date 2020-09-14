from django.db import models
from users.models import Customer
from Sites.models import Site,Booking
from django.urls import reverse

# Create your models here.

def validate_rating(value):
    if (value > 10 or value < 1):
        raise ValidationError(
            _('Rating is invalid. Enter Value between 1-10')
        )

class Site_Feedback(models.Model):
    reviewer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="User")
    reviewee = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name="Site")
    title = models.CharField(max_length=25,default="Review Title")
    content = models.TextField(max_length=250)
    rating = models.SmallIntegerField(validators=[validate_rating])
    report_choices = [
        ('R1','None'),
        ('R2','Site was not as advertised'),
        ('R3','Site location was incorrect'),
        ('R4','Site was too crowded'),
        ('R5','Pick up/Drop Time was delayed'),
        ('R6','Employee behaved inappropriately'),
        ('R7','Other (Elaborate in Report Content)'),
    ]
    report = models.CharField(
        max_length=2,
        choices = report_choices,
        default = 'R1',
    )
    valid_choices = [
        ('V','Valid'),
        ('D','Deleted'),
        ('S','Spam'),
    ]
    valid = models.CharField(
        max_length=1,
        choices = valid_choices,
        default = 'V',
    )
    
    def __str__(self):
        return self.reviewer.first_name+" "+self.reviewer.last_name+"Reviewed: "+self.reviewee.name;
    
    def get_absolute_url(self):
        return reverse('site-list')
