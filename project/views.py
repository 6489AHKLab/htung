from django.shortcuts import render, HttpResponse

# Create your views here.
def ham(req):
    return HttpResponse('hello world')
def ab(req):
    return render(req,'index.html')