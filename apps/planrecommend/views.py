from django.shortcuts import render
from .models import *
from django.views.generic import *

# planrecommend main
class SelectCityListView(View):
    template_name = 'select_city.html'

    def get(self, request, *args, **kwargs):
        counties = County.objects.all()
        context = {'counties': counties}
        return render(request, self.template_name, context)
