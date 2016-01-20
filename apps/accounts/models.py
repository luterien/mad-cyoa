from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class Account(AbstractUser):
    """
        Customized Account Model
    """
    avatar = models.ImageField(_("Profile Picture"), 
        upload_to="users/avatars/", null=True, blank=True)   
    about = models.TextField(_("About (HTML Enabled)"), null=True, blank=True)

    class Meta:
        pass

    def __unicode__(self):
        return self.username


