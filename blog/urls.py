from django.urls import path
#from this directory
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.all_blogs, name='all'),
    path('<int:blog_id>/', views.detail, name='detail'),


]
