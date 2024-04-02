from django.shortcuts import render

# Create your views here.
import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

def image_gallery(request):
    image_dir = os.path.join(settings.BASE_DIR, 'hub/static/images')
    images = os.listdir(image_dir)
    return render(request, 'index.html', {'images': images})
