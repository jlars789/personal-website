from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def testView(request):
    html = "<html><body>This is a test.</body></html>"
    return HttpResponse(html)
