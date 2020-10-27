from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def men(request):
    return render(request, 'men.html')


def mens(request):
    return render(request, 'mens.html')    


def women(request):
    return render(request, 'women.html')

def womens(request):
    return render(request, 'womens.html')    


def boys(request):
    return render(request, 'boys.html')


def girls(request):
    return render(request, 'girls.html')  
    

def about(request):
	return render(request, 'about.html')  


def blog(request):
	return render(request, 'blog.html')  

def contact(request):
	return render(request, 'contact.html')  


def checkout(request):
    return render(request, 'checkout.html')   


def payment(request):
    return render(request, 'payment.html')          

