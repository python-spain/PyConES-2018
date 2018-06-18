import os

from django.http import Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView, View


class IndexView(TemplateView):
    template_name = "index.html"


class DetailsView(View):
    base_path = 'details'

    def get(self, request, path):
        try:
            template_path = os.path.join(self.base_path, path)
            return render(request, template_path)
        except TemplateDoesNotExist:
            raise Http404()
