from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'personal/home.html')


def about(request):
    return render(request, 'personal/about.html')
	
	

def vendors(request):
    return render(request, 'personal/vendor.html')
	
	
def services(request):
    return render(request, 'personal/services.html')
	
	
def media(request):
    return render(request, 'personal/media.html')
	
	
