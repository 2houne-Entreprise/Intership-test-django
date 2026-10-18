
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('TaskFlow.urls')),
    path('projects/',include('projects.urls')),
    path(
           "projects/<int:project_pk>/tasks/",
           include("TaskManager.urls"),
       ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )