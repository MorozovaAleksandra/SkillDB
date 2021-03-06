
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from login import views

urlpatterns = [
    url(r'^login/', auth_views.LoginView.as_view(template_name='registration/login.html',
                                                 authentication_form=LoginForm), name='login'),
    url(r'^profile/', views.ProfileView.as_view(), name='profile'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='profile/profile.html', next_page=None), name='logout')
]

