from django.shortcuts import render
from .models import *
from django.views.generic import *

# planrecommend main
def planrecommend_main(request):
    return render(request, 'planrecommend_main.html')