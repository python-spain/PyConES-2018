import os
import re

from django.http import Http404
from django.shortcuts import render, redirect
from django.template import TemplateDoesNotExist
from django.urls import reverse
from django.views.generic import TemplateView, View


class IndexView(TemplateView):
    template_name = "index.html"


class DetailsView(View):
    base_path = 'details'

    def get(self, request, path):
        match = re.match(r".+/$", path)
        if match:
            path = re.sub(r"/$", "", path)
            return redirect(reverse("details", kwargs={"path": path}), permanent=True)
        try:
            template_path = "{}.html".format(os.path.join(self.base_path, path))
            return render(request, template_path)
        except TemplateDoesNotExist:
            raise Http404()
