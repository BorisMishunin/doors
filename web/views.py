from django.shortcuts import render, redirect
from sales.models import Actions
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from core.global_module import uploaded_file, extract_files, load_files
# Create your views here.

def index(request):
    params = {}
    params['actions'] = Actions.objects.all()
    return render(request, "web/index.html", params)

@csrf_exempt
def loadGoods(request):
    filename = str(request.FILES['image_file'])
    content = request.FILES['image_file']
    uploaded_file(content)
    extract_files(filename)
    load_files(filename)
    return redirect('/admin/web/goods/')

