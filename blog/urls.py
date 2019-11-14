from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

"""
=====================================
1.Here we are importing Django's function path and all of our views from the blog application 
5.The code given  tells that if someone enters to website,then views.post_list should display
Name='post_list' is the name of the URL that will be used to identify the view and 
it is important to name each URL in the app because it will be easy to remember

5.views.post_list means we are accessing the function of defined in views.py files.

6.<int:pk> means it limits the character matched and may also change the type of the variable passed to the views.
for example <int:pk> will matches  a string of integer digits and converts the value to int
======================================
Question.
1. what if we don't give 5th line?
->you will get page not found 
Using the URLconf defined in blogapps.urls, Django tried these URL patterns, in this order:

admin/
post/<int:pk>/ [name='post_detail']
post/new/ [name='post_new']
post/<int:pk>/edit/ [name='post_edit']
The empty path didn't match any of these.

bcz in admin url we have included blogs.url

========================================
Syntax:
path(route,view,kwargs=None,name=None)

"""
