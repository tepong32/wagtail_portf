from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

from django.contrib.auth import views as auth_views     # for auths for logins and logouts


urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('search/', search_views.search, name='search'),

    # # custom-pages
    # path('about/', about, name="about"),
    # path('u/', include('user.urls')),
    # path('blogs/', include('blog.urls')),
    # path('freebies/', include('freebie.urls')),


    # # django-allauth
    path('accounts/', include('allauth.urls')),
    # # ckeditor
    # path('ckeditor/', include('ckeditor_uploader.urls')),

    # # these views/html templates are inside the "user" app
    # path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login' ),
    # path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout' ),
    # path('register/', register, name='register' ),
    # path('search/', user_search_view, name="user-search"), 
    
    # # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
    #     name='password_change_done'),

    # path('password-change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
    #     name='password-change'),

    # path('password-reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
    #  name='password_reset_done'),

    # path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), name='password-reset-confirm'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset.html'), name='password-reset'),
    
    # path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
    #  name='password-reset-complete'),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]

