from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Site, Booking
from users.models import Customer
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import SiteSearchForm,BookingCreateForm, BookingUpdateEmployeeForm

class SiteListView(ListView):
    model  = Site
    #template_name = 'site/site_list.html' 
    #app/model_viewtype <- Default Naming Convention
    #ordering = ['rating']
    context_object_name = 'object'
    paginate_by = 3
    
class SiteDetailView(DetailView):
    model = Site
    paginate_by = 4
    
class SiteCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_staff

    model = Site
    fields = ['name','desc','img','number','category','price','location']
    
class SiteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_staff

    model = Site
    fields = ['name','desc','img','number','category','price','location']
    
class SiteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_staff
    
    model = Site
    success_url = "/"
    
def SiteSearchView(request):
    if request.method == 'POST':
        form = SiteSearchForm(request.POST)
        if (form.is_valid()):
            qset=form.search()
            context={
                'object': qset
            }
            return render(request, 'sites/site_search_result.html', context);
    else:
        form = SiteSearchForm()
    context = {
        'form' : form
    }
    return render(request, 'sites/site_search.html',context)

def is_custorstaff_check(user):
    if user.customer.user_type=='C' or user.is_staff:
        return True
    else:
        return False

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingCreateForm
    
    def form_valid(self,form):
        form.instance.customer = self.request.user.customer
        form.instance.employee = Customer.getAnEmployee()
        return super().form_valid(form)
    
    
class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    
class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    context_object_name = 'object'
    paginate_by = 6
    
class BookingUpdateCustomerView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingCreateForm
    context_object_name = 'object'
    template_name = 'sites/booking_update_customer.html'
    
class BookingUpdateEmployeeView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingUpdateEmployeeForm
    context_object_name = 'object'
    template_name = 'sites/booking_update_employee.html'
    
def is_emporstaff_check(user):
    if user.customer.user_type=='E' or user.is_staff:
        return True
    else:
        return False 

    
# Create your views here.
