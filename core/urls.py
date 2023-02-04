
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('follow',views.follow,name='follow'),
    path('upload',views.upload,name='upload'),
    path('search',views.search,name='search'),
    path('like-post',views.like_post,name='like-post'),
    path('signin',views.signin,name='signin'),
    path('settings',views.settings,name='settings'),
    path('logout',views.Logout,name='logout'),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
