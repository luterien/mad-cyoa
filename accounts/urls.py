from django.conf.urls import *
from django.core.urlresolvers import reverse_lazy


urlpatterns = patterns('',

    # users
    url(r'^register/$', 'accounts.views.register_user', name="register"),
    url(r'^login/$', 'accounts.views.login_user', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),

    url(r'^password_change/$', 
        'django.contrib.auth.views.password_change', 
        {'template_name': 'accounts/password_change_form.html',
        'post_change_redirect' : '/accounts/password_change/'},
        name='password_change'),
    
    url(r'^password_change/done/$', 
        'django.contrib.auth.views.password_change_done', 
        {'template_name': 'accounts/password_change_done.html'}, 
        name='password_change_done'),

    url(r'^stories/$', 'accounts.views.my_stories', name="my-stories"),

)