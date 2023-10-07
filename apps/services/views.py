from django.shortcuts import render
from django.views import View


class Service(View):
    def get(self, request, *args, **kwargs):
        # return render(request, "template_name", context)
        pass
