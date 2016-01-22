from django.shortcuts import redirect
from functools import wraps
from django.core.urlresolvers import reverse

from .models import Story


def can_edit_story(redirect_url=None):
    def decorator(function):
        def _control(request, *args, **kwargs):
            raise Exception(kwargs)
            # get story object
            story_id = kwargs.get("story_id")
            story = Story.objects.get(id=int(story_id))
            # check if the story belongs to this user
            if request.user.is_authenticated() and story in request.user.stories:
                return function(request, *args, **kwargs)
            else:
                return redirect(reverse("index"))
        return wraps(function)(_control)
    return decorator


def can_view_story():
    pass

