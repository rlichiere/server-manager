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
        if command == 'application':
            action = request.POST.get('action')
            env_id = request.POST.get('env_id')
            env = models.Environment.objects.get(id=env_id)
            if action == 'up':
                print 'ApplicationApi.post: %s up' % app
                docker.DockerCompose(application=app, environment=env).up()
                result['message'] = 'up ok.'
            elif action == 'down':
                print 'ApplicationApi.post: %s down' % app
                docker.DockerCompose(application=app, environment=env).down()
                result['message'] = 'down ok.'
            elif action == 'update':
                print 'ApplicationApi.post: %s update' % app
                pass
                result['message'] = 'update ok.'
            elif action == 'promote':
                print 'ApplicationApi.post: %s promote' % app
                pass
                result['message'] = 'promote ok.'
            elif action == 'pull':
                print 'ApplicationApi.post: %s pull' % app
                pass
                result['message'] = 'pull ok.'
            elif action == 'build':
                print 'ApplicationApi.post: %s build' % app
                docker.DockerCompose(application=app, environment=env).build()
                result['message'] = 'build ok.'
            elif action == 'start':
                print 'ApplicationApi.post: %s start' % app
                docker.DockerCompose(application=app, environment=env).start()
                result['message'] = 'start ok.'
            elif action == 'stop':
                print 'ApplicationApi.post: %s stop' % app
                docker.DockerCompose(application=app, environment=env).stop()
                result['message'] = 'stop ok.'
            elif action == 'remove':
                print 'ApplicationApi.post: %s remove' % app
                pass
                result['message'] = 'remove ok.'
            else:
                print 'ApplicationApi.post: unknown action : %s' % action
                result['status'] = 'error'
                result['message'] = 'unknown action.'
        else:
            print 'ApplicationApi.post: unknown command : %s' % command
            result['status'] = 'error'
            result['message'] = 'unknown command.'

        return HttpResponse(json.dumps(result))
