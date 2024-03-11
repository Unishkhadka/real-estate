from django.shortcuts import render
from .models import *


def index(request):
    return render(request, "spacenest/index.html")


def property(request):
    properties = Property.objects.all()
    context = {"properties": properties}
    return render(request, "spacenest/properties.html", context)
