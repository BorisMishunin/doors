from django.shortcuts import render
from sales.models import Actions

# Create your views here.

def index(request):
    params = {}
    params['actions'] = Actions.objects.all()
    return render(request, "web/index.html", params)