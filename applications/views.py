from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

import models


class ApplicationsView(LoginRequiredMixin, TemplateView):
    template_name = 'applications/applications.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicationsView, self).get_context_data(**kwargs)

        context['applications'] = models.Application.objects.all()
        context['environments'] = models.Environment.objects.all()

        return {'context': context}
