from django.http import HttpResponse    #type: ignore
from django.shortcuts import render     #type: ignore
import main.models as models

def index(request):
    val = models.Visit.objects.get(id=1)
    val.visits += 1
    val.save()
    context = {
        "visits": val.visits
    }

    return render(request, "index.html", context=context)

def testView(request):
    html = "<html><body>This is a test.</body></html>"
    return HttpResponse(html)
