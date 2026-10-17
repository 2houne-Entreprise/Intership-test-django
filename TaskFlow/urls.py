

from django.urls.conf import path

from TaskFlow.views import hello_fun, home_view, login_view, logout_view, register_view


urlpatterns = [
    path("hello",hello_fun,name="hello"),
    path("dashboard",home_view,name="dashboard"),
    path("login",login_view,name="login"),
    path("logout",logout_view,name="logout"),
    path("register",register_view,name="register"),
]