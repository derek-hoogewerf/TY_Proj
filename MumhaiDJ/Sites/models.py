from django.db import models
from PIL import Image
from django.urls import reverse
from users.models import Customer
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date, datetime, timedelta

class Site(models.Model):
    name = models.CharField(max_length=25)
    desc = models.TextField(max_length=250, verbose_name="Site Description")
    img = models.ImageField(default="def_site.jpg", upload_to="site_pics", verbose_name="Site Image")
    number = models.CharField(max_length=10, verbose_name="Contact Number")
    category_choices = [
        ('C0',"Other"),
        ('C1',"Adventure"),
        ('C2',"Historical"),
        ('C3',"Urban"),
        ('C4',"Educational"),
        ('C5',"Nature"),
        ('C6',"Event Based"),
    ]
    category = models.CharField(
        default = 'C0',
        max_length = 2,
        choices = category_choices,
    )
    price = models.FloatField()
    location = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
    def save(self):
        super().save()
        img = Image.open(self.img.path)
        if (img.height>300 or img.width>500):
            output_size = (300,500)
            img.thumbnail(output_size)
            img.save(self.img.path)
                
    def get_absolute_url(self):
        return reverse('site-detail',kwargs={'pk':self.pk})
    
    def search_filter(names,categorys,locations,sortvar):
        
        return Site.sort(Site.objects.filter(name__icontains=names).filter(category__icontains=categorys).filter(location__icontains=locations),sortvar)
    
    def sort(qset,sortvar):
        sort_dict={
            'aprice': 'price',
            'dprice': '-price',
            'aname': 'name',
            'dname': '-name',
            'randomize': '?'
        }
            
        return qset.order_by(sort_dict[sortvar])
    
    def rating(self):
        from feedback.models import Site_Feedback
        qset=Site_Feedback.objects.filter(reviewee=self.id).exclude(valid='D').exclude(valid='S');
        rating=0;
        n=0;
        for q in qset:
            rating+=q.rating
            n+=1
        if n!=0:
            return round(rating/n,2)
        else:
            return 0
    
    def reviews(self):
        from feedback.models import Site_Feedback
        qset=Site_Feedback.objects.filter(reviewee=self.id);
        return qset
    
def validate_date(value):
    if (value > date.today()+ timedelta(days=60) or value < date.today()):
        raise ValidationError(
            _('Date is invalid')
        )
        
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='CX'); 
    employee = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='EMP'); 
    site = models.ForeignKey(Site, on_delete=models.CASCADE); 
    date = models.DateField(validators=[validate_date]);
    pickloc = models.TextField(verbose_name="Pick Up Location");
    droploc = models.TextField(verbose_name="Drop Location");
    status_choices = [
        ('P','Pending Confirmation'),
        ('B','Booked'),
        ('I','In Progress'),
        ('C','Completed'),
        ('R','Removed'),
    ]
    status = models.CharField(
        max_length = 1,
        choices = status_choices,
        default = 'P',
    )
    
    def __str__(self):
        return self.customer.first_name+" "+self.customer.last_name+" Booking: "+self.site.name 
    
    def get_absolute_url(self):
        return reverse('site-book-detail',kwargs={'pk':self.pk})
    
    def getSelfEmployee(form):
        return form.instance.employee
    