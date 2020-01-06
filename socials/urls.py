from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url 
from .import views

from django.contrib.auth import views as auth_views

urlpatterns=[
    
    
    url('', views.signup, name='signup'),
    url(r'^home/', views.home, name = 'home'),
    url(r'^login/', auth_views.LoginView.as_view(template_name = 'auth/login.html'), name = 'login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='auth/thankyou.html'), name = 'logout'),
    url(r'^profile/', views.profile , name = 'my_profile'),
    url(r'^image/new', views.createimage.as_view(), name = 'post'),
    url(r'^comment/(?P<image_id>\d+)$',views.comments,name='comments'),
    url(r'^like/$',views.like_post,name='like_post'),
    url(r'^delete/(?P<image_id>\d+)$',views.delete,name='delete'),
    url(r'^update/',views.update_profile,name='update_profile'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)