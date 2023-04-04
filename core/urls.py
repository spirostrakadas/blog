from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('post/<str:pk>/',views.detail,name='detail'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('create_post/',views.newPost,name='create_post'),
     path('<str:pk>/delete/',views.delete,name='delete'),
     path('logout/',views.logout ,name='logout'),
     path('<str:pk>/profile',views.MyProfile,name='myprofile')
]


