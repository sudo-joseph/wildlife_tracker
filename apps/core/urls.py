from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('map/', views.map, name='map'),
    path('report/', views.report, name="map"),
    path('add-new/', views.add_new, name='add_new'),
]
