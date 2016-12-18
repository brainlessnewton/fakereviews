from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
# Create your views here.

def index(request):
	return render(request, 'index.html', {})