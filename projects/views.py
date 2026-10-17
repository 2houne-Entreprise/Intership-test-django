from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import  reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView
)

from projects.forms import ProjectForm
from projects.models import Project

class ProjectListView(LoginRequiredMixin,ListView):
    model=Project
    template_name="projets/list_view.html"
    context_object_name="projets"

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class  ProjectCreateView(LoginRequiredMixin,CreateView):
    model=Project
    form_class=ProjectForm
    template_name="projets/project_form.html"
    success_url=reverse_lazy("projets:list")


    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)



class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model=Project
    form_class=ProjectForm
    template_name="projets/project_form.html"
    success_url=reverse_lazy("projets:list")


    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)



class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model=Project
    template_name="projets/project_confirm_delete_form.html"
    success_url=reverse_lazy("projets:list")


    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    
    
    