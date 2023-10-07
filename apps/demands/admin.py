from django.contrib import admin

from project.utils import register_app_models_on_admin

from . import models

# in case of needing custom ModelAdmin classes, must be added manually before function call

app_name = __package__.split(".")[-1]
register_app_models_on_admin(app_name)
