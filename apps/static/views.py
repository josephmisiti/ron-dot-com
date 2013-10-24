
from django.shortcuts import render

def index(request):
	return render(request, 'static/index.html', {})
	
def portfolio(request):
	return render(request, 'static/portfolio.html', {})
	
def videos(request):
	return render(request, 'static/videos.html', {})
	
def contact(request):
	return render(request, 'static/contact.html', {})
	
def portfolio_one(request): return render(request, 'rostam_1.html', {})

def portfolio_two(request): return render(request, 'robert.html', {})

def portfolio_three(request): return render(request, 'rostam_2.html', {})

def portfolio_four(request): return render(request, 'rostam_3.html', {})

def portfolio_five(request): return render(request, 'joey.html', {})

def portfolio_six(request): return render(request, 'lenny.html', {})