import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import View, TemplateView

import models
from hostmanager.utils import docker

class ApplicationsView(LoginRequiredMixin, TemplateView):
    template_name = 'applications/applications.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicationsView, self).get_context_data(**kwargs)

        context['applications'] = models.Application.objects.all()
        context['environments'] = models.Environment.objects.all()

        return {'context': context}


class ApplicationApi(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        result = dict()
        app_id = kwargs['app_id']
        app = models.Application.objects.get(id=app_id)

        result['application'] = app.jsonify

        return HttpResponse(json.dumps(result))

    def post(self, request, *args, **kwargs):
        result = {'status': 'success', 'message': ''}
        app_id = kwargs['app_id']
        app = models.Application.objects.get(id=app_id)

        command = request.POST.get('command')
        action = request.POST.get('action')
        env_id = request.POST.get('env_id')
        env = models.Environment.objects.get(id=env_id)
        if command == 'application':
            if action == 'up':
                print 'ApplicationApi.post: %s up' % app
                docker.DockerCompose(application=app, environment=env).up()
                result['message'] = 'up ok.'
            elif action == 'down':
                print 'ApplicationApi.post: %s down' % app
                result['message'] = 'down ok.'
            else:
                print 'ApplicationApi.post: unknown action : %s' % command
                result['status'] = 'error'
                result['message'] = 'unknown action.'

        return HttpResponse(json.dumps(result))
