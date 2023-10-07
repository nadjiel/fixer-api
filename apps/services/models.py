from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base_app.models import BaseModel


class ServiceManager(models.Manager):
    pass  # define your manager methods here


class Service(BaseModel):
    # manager
    objects = ServiceManager()

    # define your fields here
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    sections = models.JSONField(default=list)
