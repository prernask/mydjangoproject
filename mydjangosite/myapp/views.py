from django.shortcuts import render
from .models import User


# Create your views here.
def index(request):
    return render(request, "myapp/index.html", {})


def userreg(request):
    return render(request, "myapp/userreg.html", {})


def insertuser(request):
    vid = request.POST['uid'];
    # post method to fetch value
    name = request.POST['uname'];
    # uid, uname similar to user_reg html file
    email = request.POST['uemail'];
    contact = request.POST['ucontact'];
    # user class
    # inside set values left side=column name inside sql table, right side=template variable created in user class
    # left side uid exactly matching from mysql table
    us = User(uid=vid, uname=name, uemail=email, ucontact=contact);
    us.save();
    return render(request, 'myapp/index.html', {})

    # we are fetching the value from tyd from the template then we are storing this value into a temporary variabl
    # inside the view and then from view we are setting into the mysql column

# this is how we are fetching from the front end template uh getting inside the views and then from view we are
# sending it to the mysql column
