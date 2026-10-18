from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib import messages
from .forms import TaskForm
from .models import Task
from projects.models import Project
from django.shortcuts import get_object_or_404, redirect
from projects.mixins import ProjectOwnerRequiredMixin




class TaskListView(LoginRequiredMixin,ListView):
    model=Task
    template_name="projets/project_detais.html"
    context_object_name="tasks"

    def get_queryset(self):
        self.project=get_object_or_404(Project,pk=self.kwargs["project_pk"],user=self.request.user)
        
        return Task.objects.filter(project=self.project).select_related("project").order_by("deadline","title")

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["project"]=self.project
        return context
        

class TaskCreateView(ProjectOwnerRequiredMixin,CreateView):
    model=Task
    form_class=TaskForm
    template_name="tasks/task_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.project=get_object_or_404(Project,pk=self.kwargs["project_pk"],user=request.user)
        return super().dispatch(request,*args,**kwargs)


    def form_valid(self, form):
        form.instance.project=self.project
        response=super().form_valid(form)
        messages.success(self.request,"Tache cree avec succes")
        return response

    def get_success_url(self):
        return reverse_lazy(
                "tasks:list",
                kwargs={"project_pk": self.project.pk},
            )
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["project"] = self.project
        return context



  
class TaskUpdateView(ProjectOwnerRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"

    def get_queryset(self):
        return Task.objects.filter(project__user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("tasks:list",kwargs={"project_pk":self.object.project.pk})



class TaskDaleteView(ProjectOwnerRequiredMixin,DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"

    def get_queryset(self):
        return Task.objects.filter(project__user=self.request.user,project_id=self.kwargs["project_pk"])

    def get_success_url(self):
        return reverse_lazy("tasks:list",kwargs={"project_pk":self.object.project.pk})





class TaskStatusUpdateView(ProjectOwnerRequiredMixin, View):
    

    def post(self, request, project_pk, pk):
        task = get_object_or_404(
            Task.objects.filter(
                project__user=request.user,
                project_id=project_pk,
            ),
            pk=pk,
        )

        new_status = request.POST.get("status")

        if new_status in Task.Status.values:
            task.status = new_status
            task.save(update_fields=["status", "updated_at"])
            messages.success(
                request,
                "Statut de la tâche modifié avec succès.",
            )
        else:
            messages.error(request, "Statut invalide.")

        return redirect(
            "tasks:list",
            project_pk=project_pk,
        )



      