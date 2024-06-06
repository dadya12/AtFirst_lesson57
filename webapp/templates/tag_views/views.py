from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from webapp.models import Tag, Projects
from webapp.forms import TagForms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class TagCreate(PermissionRequiredMixin, CreateView):
    template_name = 'tags/tag_create.html'
    model = Tag
    form_class = TagForms
    permission_required = 'webapp.add_tag'

    def has_permission(self):
        projects = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in projects.users.all()

    def get_success_url(self):
        return reverse('webapp:detail_project', kwargs={'pk': self.object.projects.pk})

    def form_valid(self, form):
        projects = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        tag = form.save(commit=False)
        tag.project = projects
        tag.save()
        form.save_m2m()
        return redirect('webapp:detail_project', pk=projects.pk)


class TagUpdate(PermissionRequiredMixin, UpdateView):
    model = Tag
    form_class = TagForms
    template_name = 'tags/tag_update.html'
    permission_required = 'webapp.change_tag'

    def has_permission(self):
        tag = self.get_object()
        return super().has_permission() and self.request.user in tag.project.users.all()

    def get_success_url(self):
        return reverse('webapp:tag_detail', kwargs={'pk': self.object.pk})


class TagDetail(LoginRequiredMixin, DetailView):
    model = Tag
    template_name = 'tags/detail_tag.html'


class TagDelete(PermissionRequiredMixin, DeleteView):
    model = Tag
    template_name = 'tags/tag_delete.html'
    permission_required = 'webapp.delete_tag'

    def has_permission(self):
        tag = self.get_object()
        return super().has_permission() and self.request.user in tag.project.users.all()

    def get_success_url(self):
        return reverse('webapp:home')
