from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from servermanager import settings


class ConfigView(LoginRequiredMixin, TemplateView):
    template_name = 'core/config.html'

    def get_context_data(self, **kwargs):
        context = super(ConfigView, self).get_context_data(**kwargs)

        context['config'] = dict()
        context['config']['basic'] = settings.config.get_basic_configuration()
        context['config']['environment'] = settings.config.get_environment_configuration()

        context['config']['file'] = list()
        for conf_file in settings.config.get_config_file_list:
            context['config']['file'].append({
                'key': conf_file['path'],
                'data': settings.config.get_file_configuration(conf_file['path'])
            })

        context['config']['database'] = settings.config.get_database_configuration()
        context['config']['complete'] = settings.config.get_config

        return {'context': context}
