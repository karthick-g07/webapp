from django.urls import path
from .import views
print('checking')
urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
     path('forgetpage/', views.forget_view, name='forgetpage'),
]