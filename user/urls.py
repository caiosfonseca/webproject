from django.conf.urls import url


urlpatterns = [
    url(
        r'login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'user/login.html'
        },
        name='login'
    ),

    url(
        r'logout/$',
        'django.contrib.auth.views.logout',
        {
            'next_page': 'user:login'
        },
        name='logout'
    ),

    url(
        r'password_reset/$',
        'django.contrib.auth.views.password_reset',
        {
            'template_name': 'user/password_reset.html',
            'email_template_name': 'user/password_reset_email.html',
            'post_reset_redirect': 'user:password_reset_done'
        },
        name="password_reset"
    ),

    url(
        r'password_reset_done/$',
        'django.contrib.auth.views.password_reset_done',
        {
            'template_name': 'user/password_reset_done.html'
        },
        name='password_reset_done'
    ),

    url(
        r'password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/\
            (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {
            'post_reset_redirect': 'user:password_reset_complete',
            'template_name': 'user/password_reset_confirm.html'
        },
        name='password_reset_confirm'
    ),

    url(
        r'^password_done/$',
        'django.contrib.auth.views.password_reset_complete',
        {
            'template_name': 'user/password_reset_complete.html'
        },
        name='password_reset_complete'
    ),

    # url(r'change_password/$', login, name='change_password'),
    # url(r'register/$', login, name='register'),
    # url(r'edit/$', login, name='edit'),
]