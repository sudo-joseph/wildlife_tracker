from django.urls import path

from apps.core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add-new/', views.add_new, name='add_new'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('list-view/', views.list_view, name='list_view'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('log_location/', views.log_location, name="log_location"),
    path('address/', views.address, name="log_location"),
]
