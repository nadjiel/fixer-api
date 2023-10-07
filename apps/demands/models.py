from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base_app.models import BaseModel

from django.conf import settings

import random, string

USER_MODEL_AS_STRING = settings.AUTH_USER_MODEL


class DemandManager(models.Manager):
    pass  # define your manager methods here


class Demand(BaseModel):
    class StatusChoices(models.IntegerChoices):
        OPENED = 0, "Aberto"
        IN_PROGRESS = 1, "Em Andamento"
        COMPLETE = 2, "Concluido"
        REFUSED = 3, "Recusado"

    # manager
    objects = DemandManager()

    # define your fields here
    text = models.TextField()
    user = models.ForeignKey(
        USER_MODEL_AS_STRING, on_delete=models.CASCADE, blank=True, null=True
    )
    code = models.CharField(max_length=10, blank=True, editable=False)
    status = models.IntegerField(
        choices=StatusChoices.choices, default=StatusChoices.OPENED
    )

    def save(self, *args, **kwargs):
        if self.pk is None:
            code_length = 10
            characters = string.ascii_letters + string.digits

            code = "".join(random.choice(characters) for _ in range(code_length))

            while self.__class__.objects.filter(code=code).exists():
                code = "".join(random.choice(characters) for _ in range(code_length))

            self.code = code

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.code
