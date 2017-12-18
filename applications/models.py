from __future__ import unicode_literals

from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=50, blank=False)
    label = models.CharField(max_length=100, blank=False)
    git_repository_url = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return str(self.name)

    @property
    def jsonify(self):
        return {
            'name': self.name,
            'label': self.label,
            'git_repository_url': self.git_repository_url,
        }

class Environment(models.Model):
    name = models.CharField(max_length=50, blank=False)
    label = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.name)
