from django.shortcuts import render

from django.views.generic import View, TemplateView
import models


class ApplicationsView(TemplateView):
    template_name = 'containermanager/applications.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicationsView, self).get_context_data(**kwargs)

        apps = models.Application.objects.all()
        context['applications'] = apps

        return {'context': context}
