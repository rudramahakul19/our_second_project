from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def silk(request):
    return HttpResponse("<h1><marquee>hii,, i am silk how are you</h1></marquee>")
    