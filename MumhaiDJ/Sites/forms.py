from django.forms import ModelForm, widgets
from .models import Site, Booking
from users.models import Customer
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

sort_choices=(
    ('aname', 'Alphabetical'),
    ('dname', 'Reverse Alphabetical'),
    ('aprice',"Price (Low to High)"),
    ('dprice',"Price (High to Low)"),
    ('randomize',"Random")
)

class SiteSearchForm(forms.ModelForm):
    category_choices = [
        ('',"Any"),
        ('C1',"Adventure"),
        ('C2',"Historical"),
        ('C3',"Urban"),
        ('C4',"Educational"),
        ('C5',"Nature"),
        ('C6',"Event Based"),
        ('C0',"Other"),
    ]
    sort = forms.ChoiceField(choices=sort_choices)
    category = forms.ChoiceField(choices=category_choices)
    
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(SiteSearchForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = False
        self.fields['category'].required = False
        self.fields['location'].required = False
        self.fields['sort'].required = False
    
    class Meta:
        model =  Site
        fields = ['name','category','location']
        #location_choices = Booking.location_choices
        widgets = {
            #'location':widgets.Select()
        }
        
    
    def search(self):
        return Site.search_filter(self.cleaned_data.get('name'),
                                  self.cleaned_data.get('category'),
                                  self.cleaned_data.get('location'),
                                  self.cleaned_data.get('sort'))
        
    #do a forms.Form, enter the fields needed, define a method search which will just call Site.search_sort(),render a template for search that is a list view with the new query set
    
class BookingCreateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['site','date','pickloc','droploc']
        widgets = {
            'date' : widgets.DateInput(attrs={'type': 'date'}),
            #'customer' : widgets.HiddenInput(),
            #'employee' : widgets.HiddenInput(),
            #'status' : widgets.HiddenInput(),
        }
        def form_valid(form,self):
            form.instance.customer = self.request.user.id
            form.instacen.status = 'P'
            form.instance.employee = Customer.getAnEmployee()
            return super().form_valid(form)
        
class BookingUpdateEmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ['status']
        status_update_choices = [
        ('P','Pending Confirmation'),
        ('B','Booked'),
        ('I','In Progress'),
        ('C','Completed'),
    ]
        widgets = {
            'status' : widgets.Select(choices=status_update_choices),
        }
        
        
        
    #checks to do: Emp is available, Cust is available, Date is Valid    
        #return super().form_valid(form)