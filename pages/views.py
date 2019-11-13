from django.shortcuts import render
from django.http import HttpResponse

def home_view(*args, **kwargs):
	return HttpResponse("<h1>Welcome to Fitbit</h1>")
# Create your views here.
