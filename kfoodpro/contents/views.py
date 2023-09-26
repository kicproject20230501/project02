from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from .models import Food, Feedback

# Create your views here.
def start(request):
    return render(request, 'contents/start.html')

def loading(request):
    return render(request, 'contents/loading.html')

def result(request):
    return render(request, 'contents/result.html')

def wrong(request):
    return render(request, 'contents/wrong.html')