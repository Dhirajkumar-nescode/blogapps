"""
Author:ARYADRJ

1.View is the place where we write the logic of out application
and view will request the information from the models and pass it to template.
"""
from django.shortcuts import render
# Create your views here.


def post_list(request):
    return render(request,"blog/post_list.html",{})

"""
The code given above, we have created function called post_list that takes request
and will return the value it gets from calling another function render that will render
our template
"""
