from __future__ import unicode_literals

from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=10, blank=False)
    label = models.CharField(max_length=20, blank=False)
    git_repository_url = models.CharField(max_length=200, blank=False)

class Environment(models.Model):
    name = models.CharField(max_length=10, blank=False)
    label = models.CharField(max_length=20, blank=False)
