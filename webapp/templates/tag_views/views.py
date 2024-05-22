from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from webapp.models import Tag, Projects
from webapp.forms import TagForms


class TagCreate(CreateView):
    template_name = 'tags/tag_create.html'
    model = Tag
    form_class = TagForms

    def get_success_url(self):
        return reverse('detail_project', kwargs={'pk': self.object.projects.pk})

    def form_valid(self, form):
        projects = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        tag = form.save(commit=False)
        tag.project = projects
        tag.save()
        form.save_m2m()
        return redirect('detail_project', pk=projects.pk)


class TagUpdate(UpdateView):
    model = Tag
    form_class = TagForms
    template_name = 'tags/tag_update.html'

    def get_success_url(self):
        return reverse('tag_detail', kwargs={'pk': self.object.pk})


class TagDetail(DetailView):
    model = Tag
    template_name = 'tags/detail_tag.html'


class TagDelete(DeleteView):
    model = Tag
    template_name = 'tags/tag_delete.html'

    def get_success_url(self):
        return reverse('home')

