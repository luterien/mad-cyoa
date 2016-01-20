from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class Account(AbstractUser):
    """
        Customized Account Model
    """
    avatar = models.ImageField(upload_to="users/avatars/", null=True, blank=True)   
    about = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.username
