from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse("Hello, world. You're at the polls index")


def search(request):
	data={'name': 'Ahmad',
		'post' : 'SE'}
	return render (request, 'new_template.html', data)
# Create your views hre.
