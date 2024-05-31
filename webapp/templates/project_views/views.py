from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Projects
from webapp.forms import SearchForm, ProjectUserForm
from django.db.models import Q
from django.utils.http import urlencode
from webapp.forms import ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class IndexView(ListView):
    model = Projects
    template_name = 'projects/home.html'
    context_object_name = 'projects'
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.search_form = SearchForm(request.GET)
        self.search_value = None
        if self.search_form.is_valid():
            self.search_value = self.search_form.cleaned_data['search']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class ProjectDetail(LoginRequiredMixin, DetailView):
    model = Projects
    template_name = 'projects/project_detail.html'


class ProjectCreate(PermissionRequiredMixin, CreateView):
    template_name = 'projects/project_create.html'
    model = Projects
    form_class = ProjectForm
    permission_required = 'webapp.add_projects'

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        form.instance.users.add(self.request.user)
        return response

    def get_success_url(self):
        return reverse('webapp:detail_project', kwargs={'pk': self.object.pk})


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    model = Projects
    form_class = ProjectForm
    template_name = 'projects/project_update.html'
    permission_required = 'webapp.change_projects'

    def get_success_url(self):
        return reverse('webapp:detail_project', kwargs={'pk': self.object.pk})


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    model = Projects
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('webapp:home')
    permission_required = 'webapp.delete_projects'


class UpdateUserView(PermissionRequiredMixin, UpdateView):
    model = Projects
    form_class = ProjectUserForm
    template_name = 'update_user.html'
    context_object_name = 'projects'
    permission_required = 'auth.change_user'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('webapp:detail_project', kwargs={'pk': self.object.pk})
