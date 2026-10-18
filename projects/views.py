from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import  reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    DeleteView,
    UpdateView
)
from .mixins import ProjectOwnerRequiredMixin

from projects.forms import ProjectForm
from projects.models import Project

class ProjectListView(LoginRequiredMixin,ListView):
    model=Project
    template_name="projets/list_view.html"
    context_object_name="projets"

    def get_queryset(self):
        return Project.objects.all()

class  ProjectCreateView(LoginRequiredMixin,CreateView):
    model=Project
    form_class=ProjectForm
    template_name="projets/project_form.html"
    success_url=reverse_lazy("projets:list")


    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)



class ProjectUpdateView(ProjectOwnerRequiredMixin,UpdateView):
    project_kwarg="pk"
    
    model=Project
    form_class=ProjectForm
    template_name="projets/project_form.html"
    success_url=reverse_lazy("projets:list")


    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)
        


class ProjectDeleteView(ProjectOwnerRequiredMixin,DeleteView):
    model=Project
    template_name="projets/project_confirm_delete_form.html"
    success_url=reverse_lazy("projets:list")


    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    
    
    
    
class ProjectDetaiView(LoginRequiredMixin,DetailView):
    model=Project
    template_name="projets/project_detais.html"
    context_object_name="project"


    def get_queryset(self):
        return Project.objects.all()
    
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)    
        context["tasks"]=self.object.tasks.all()
        return context
    