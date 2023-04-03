from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('post/<str:pk>/',views.detail,name='detail'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin')

]
