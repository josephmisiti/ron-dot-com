
from django.shortcuts import render

def index(request):
	return render(request, 'static/index.html', {})
	
def portfolio(request):
	return render(request, 'static/portfolio.html', {})
	
def videos(request):
	return render(request, 'static/videos.html', {})
	
def contact(request):
	return render(request, 'static/contact.html', {})
	
def portfolio_one(request): return render(request, 'static/contact.html', {})

def portfolio_two(request): return render(request, 'static/contact.html', {})

def portfolio_three(request): return render(request, 'static/contact.html', {})

def portfolio_four(request): return render(request, 'static/contact.html', {})

def portfolio_five(request): return render(request, 'static/contact.html', {})