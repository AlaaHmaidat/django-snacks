from django.shortcuts import render
from django.views.generic import TemplateView

class DarkPageView(TemplateView):
    template_name = 'dark.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_info'] = "Additional information"
        return context