

from django.urls import path,include

from .views import ProjectCreateView, ProjectDeleteView, ProjectDetaiView, ProjectListView, ProjectUpdateView

app_name = "projets"
urlpatterns = [
    path("",ProjectListView.as_view(),name="list"),
    path("create/",ProjectCreateView.as_view(),name="create"),
    path("<int:pk>/update/",ProjectUpdateView.as_view(),name="update"),
    path("<int:pk>/delete/",ProjectDeleteView.as_view(),name="delete"),
    path("<int:pk>/", ProjectDetaiView.as_view(), name="detail"),
]

