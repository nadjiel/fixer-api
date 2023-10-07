from uuid import uuid4

from django.db import models


class BaseModel(models.Model):

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
