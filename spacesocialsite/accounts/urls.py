from django.urls import re_path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [

re_path(r'^login/$',LoginView.as_view(template_name='accounts/login.html'),name='login'),
re_path(r'^logout/$',LogoutView.as_view(),name='logout'),
re_path(r'^signup/$',views.Signup.as_view(),name='signup'),

]
