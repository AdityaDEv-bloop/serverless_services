
from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponseRedirect
from easyship.utils import ValidateUser,get_tokens_for_user
from django.contrib.auth import login
import requests

session = requests.session()
class ApiLoginForm(forms.Form):
    email = forms.CharField(label="email", max_length=100)
    password = forms.CharField(label="password", max_length=500)

def Home(request):
    print("create a form instance and populate it with data from the request")
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        print("create a form instance and populate it with data from the request")
        form = ApiLoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = ValidateUser(Email=form.data['email'], Password=form.data['password'])
            if user is not None and user.is_admin:
                login(request, user=user)
                authdata = get_tokens_for_user(user=user)
                resp = session.get(
                    url="http://127.0.0.1:8000/api/v1/ship-easy/swagger/?openapi=JSON",
                    headers={ "Authorization": "Bearer {0}".format(authdata["access"]) }
                )
                return redirect('http://127.0.0.1:8000/api/v1/ship-easy/swagger/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ApiLoginForm()

    return render(request, "../templates/index.html",{"form": form})

