
from django.shortcuts import render

def index(request):
	
	return render(request, 'static/index.html', {})
	
def portfolio(request):
	
	return render(request, 'static/portfolio.html', {})
	
def contact(request):
	
	return render(request, 'static/contact.html', {})