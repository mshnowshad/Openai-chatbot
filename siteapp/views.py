# from email import message
# from urllib import response
from django.http import JsonResponse
from django.shortcuts import render

# from django.http import HttpResponse
# Create your views here.

def home(request):
	if request.method == 'POST':
		message = request.POST.get('message')
		response = 'Hi this is my response'
		return JsonResponse({'message':message,'response':response})
	return render(request,'index.html')

# 34:02 times is off
