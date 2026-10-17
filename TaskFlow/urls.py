

from django.urls.conf import path

from TaskFlow.views import hello_fun


urlpatterns = [
    path("hello",hello_fun,name="hello"),
]