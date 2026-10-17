

from django.urls import path,include

from .views import ProjectCreateView, ProjectListView, ProjectUpdateView

urlpatterns = [
    path("",ProjectListView.as_view,name="list"),
    path("create/",ProjectCreateView.as_view,name="create"),
    path("<int:pk>/update/",ProjectUpdateView.as_view,name="update"),
    path("<int:pk>/delete/",ProjectUpdateView.as_view,name="delete"),
]

