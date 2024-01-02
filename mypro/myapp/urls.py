from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('user_view/',views.get_user_profile, name='get_user_profile'),
]