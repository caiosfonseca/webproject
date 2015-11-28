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
            'post_reset_redirect': 'user:logout'
        },
        name='password_reset'
    ),

    # url(r'change_password/$', login, name='change_password'),
    # url(r'register/$', login, name='register'),
    # url(r'edit/$', login, name='edit'),
]
