from django.conf.urls import url
from . import views

from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
          url(r'^$', views.root, name = 'root'),
          url(r'^login/$', login, {'template_name' : 'optic/login.html'}, name = 'login'),
          url(r'^logout/$', logout, {'template_name' : 'optic/logout.html'}, name = 'logout'),
          url(r'^register/$', views.register_view, name = 'register'),
          url(r'^profile/$', views.user_profile, name = 'user_profile'),
          url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),
          url(r'^edit-password/$', views.edit_password, name = 'edit_password'),


          url(r'^reset-password/$', password_reset, { 'template_name' : 'optic/reset_password.html', 'post_reset_redirect': 'optic:password_reset_done', 'email_template_name': 'optic/reset_password_email.html'  }, name = 'reset_password'),
          url(r'^reset-password/done/$', password_reset_done,  name = 'password_reset_done'),

          url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, { 'template_name' : 'optic/reset_password_confirm.html', 'post_reset_redirect': 'optic:password_reset_complete'}, name = 'password_reset_confirm'),
          url(r'^reset-password/complete/$', password_reset_complete, {'template_name' :'optic/reset_password_complete.html'},
		name = 'password_reset_complete')

]
