
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users.views import register, profile, validateUsername, validateEmail
from django.conf.urls.static import static
from django.conf import settings
from advance import views as aviews
from middleware_demo import views as mviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/', profile, name='profile'),
    path('dyn/', include('dynamic.urls')),
    path('validate-username/', validateUsername, name="validate-username"),
    path('validate-email/', validateEmail, name='validate-email'),

    # advance app url
    path("image/", aviews.unruly_passengers_csv, name='image'),


    #middleware_demo app
    path("demo/",  mviews.index, name="demo"),

    #ajaxdemo
    path('rooms/', include('rooms.urls')),

    #social_django
    path('oauth/', include('social_django.urls', namespace='social')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)