from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Projects
from webapp.forms import SearchForm
from django.db.models import Q
from django.utils.http import urlencode
from webapp.forms import ProjectForm


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


class ProjectDetail(DetailView):
    model = Projects
    template_name = 'projects/project_detail.html'


class ProjectCreate(CreateView):
    template_name = 'projects/project_create.html'
    model = Projects
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.pk})


class ProjectUpdate(UpdateView):
    model = Projects
    form_class = ProjectForm
    template_name = 'projects/project_update.html'

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.pk})


class ProjectDelete(DeleteView):
    model = Projects
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('home')
