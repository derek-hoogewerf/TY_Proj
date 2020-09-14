from django.urls import path
from .views import SiteListView, SiteDetailView, SiteCreateView, SiteUpdateView, SiteDeleteView, SiteSearchView, BookingCreateView, BookingDetailView, BookingListView, BookingUpdateCustomerView, BookingUpdateEmployeeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', SiteListView.as_view(), name='site-list'),
    path('<int:pk>', SiteDetailView.as_view(), name='site-detail'),
    path('<int:pk>/update', SiteUpdateView.as_view(), name='site-update'),
    path('<int:pk>/delete', SiteDeleteView.as_view(), name='site-delete'),
    path('new', SiteCreateView.as_view(), name='site-create'),
    path('search',SiteSearchView,name='site-search'),
    path('booking/new',BookingCreateView.as_view(),name='site-book-create'),
    path('booking/<int:pk>',BookingDetailView.as_view(),name='site-book-detail'),
    path('booking/',BookingListView.as_view(),name='site-book-list'),
    path('booking/<int:pk>/update',BookingUpdateCustomerView.as_view(),name='site-book-update'),
    path('booking/<int:pk>/update/emp',BookingUpdateEmployeeView.as_view(),name='site-book-update-emp'),
]