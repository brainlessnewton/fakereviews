from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def login(request):
	return render(request, 'login.html', {})

def register(request):
	return render(request, 'register.html', {})

def upload(request):
	return render(request, 'upload.html', {})

def contact(request):
	return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})