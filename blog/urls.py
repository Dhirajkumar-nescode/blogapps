#Here we are importing Django's function path and all of our views from the blog application 
from django.urls import path
from . import views
"""
    1.The code given below tells that if someone enters to website,then views.post_list should display
    2.Name='post_list' is the name of the URL that will be used to identify the view and 
      it is important to name each URL in the app because it will be easy to remember
"""

urlpatterns=[
   
    path('',views.post_list, name='post_list'),
]
