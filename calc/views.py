from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,"home.html",{'name':'Arpit'})

def add(request):
	a=int(request.GET['num1'])
	b=int(request.GET['num2'])
	res=a+b
	return render(request,"result.html",{'result':res})
