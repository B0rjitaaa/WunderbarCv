from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

def index(request):
	response = {}
	return render(request, 'index.html', response)

def bio(request):
	response = {}
	return render(request, 'bio.html', response)

def works(request):
	response = {}
	return render(request, 'works.html', response)
