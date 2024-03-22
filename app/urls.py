from django.contrib import admin
from django.urls import path
from .views import home, register, login_user, logout_user, scifi, fantasy, anime, about, contact

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name="register"),        # URL for registration
    path('login/', login_user, name="login_user"),       # URL for login
    path('logout/', logout_user, name="logout_user"),    # URL for logout
    path('fantasy/', fantasy, name='fantasy'),
    path('scifi/', scifi, name='scifi'),
    path('anime/', anime, name='anime'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
