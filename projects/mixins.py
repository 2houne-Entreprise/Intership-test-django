from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from projects.models import Project
from django.contrib import messages


class ProjectOwnerRequiredMixin(LoginRequiredMixin):
    project_kwarg="project_pk"

    def dispatch(self, request, *args, **kwargs):
        project_pk=kwargs.get(self.project_kwarg) 
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if project_pk is None:
            project=get_object_or_404(Project,pk=project_pk)


            if project.user_id != request.user.id:
                messages.error(request,"Vous n'êtes pas autorisé à effectuer cette opération." )
                return redirect("projets:list")
                
            self.project=project
        return super().dispatch(request, *args, **kwargs)