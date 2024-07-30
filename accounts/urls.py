from django.urls import path
from . import views

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("test-token", views.test_token, name="test_token")
]
