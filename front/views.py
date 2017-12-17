from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class ReadmeView(LoginRequiredMixin, TemplateView):
    template_name = 'front/readme.html'

    def get_context_data(self, **kwargs):
        context = super(ReadmeView, self).get_context_data(**kwargs)

        with open('README.md') as file:
            file_content = ''
            for line in file:
                file_content += line + '<br />'
        context['readme_content'] = file_content

        return {'context': context}
