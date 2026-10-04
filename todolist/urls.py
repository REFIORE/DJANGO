from django.contrib import admin
from django.urls import path
from todo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('monday', views.monday),
    path('tuesday', views.tuesday),
    path('wednesday', views.wednesday),
    path('thursday', views.thursday),
    path('friday', views.friday),
    path('saturday', views.saturday),
    path('sunday', views.sunday),
]
