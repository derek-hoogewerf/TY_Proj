from django.shortcuts import render,redirect
from django.forms import widgets
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Site_Feedback
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import SiteFeedbackCreateForm
from django.urls import reverse
# Create your views here.

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Site_Feedback
    form_class = SiteFeedbackCreateForm
    context_object_name = 'object'
    template_name = 'feedback/feedback_form.html'
    
    def form_valid(self,form):
        form.instance.reviewer = self.request.user.customer
        return super().form_valid(form)