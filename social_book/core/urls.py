from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name = 'settings'),
    path('upload', views.upload, name = 'upload'),
    path('follow', views.follow, name = 'follow'),
    path('search', views.search, name = 'search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name = 'upload'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('post/<uuid:post_id>/comment', views.post_comment, name='post_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('delete_post/<uuid:post_id>/', views.delete_post, name='delete_post')
]