from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('/<str:pk>/',views.detail,name='detail')
]
