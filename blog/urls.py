from django.urls import path
#from this directory
from blog import views

urlpatterns = [
    path('', views.all_blogs, name = 'all'),

]
