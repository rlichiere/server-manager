from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from utils import shell

class HostManagerView(LoginRequiredMixin, TemplateView):
    template_name = 'hostmanager/hostmanager.html'

    def get_context_data(self, **kwargs):
        context = super(HostManagerView, self).get_context_data(**kwargs)

        context['free_memory'] = shell.get_free_memory()

        return {'context': context}
