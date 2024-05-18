from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View, FormView
from webapp.models import Tag
from webapp.forms import TagForms


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.all()
        return context


class TagView(TemplateView):
    template_name = 'detail_tag.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, pk=kwargs.get('pk'))
        return context


class TagCreateView(FormView):
    form_class = TagForms
    template_name = 'tag_create.html'

    def form_valid(self, form):
        types = form.cleaned_data.pop('type')
        statuss = form.cleaned_data.pop('status')
        self.tags = Tag.objects.create(
            summary=form.cleaned_data.get('summary'),
            description=form.cleaned_data.get('description'),
        )
        self.tags.type.set(types)
        self.tags.status.set(statuss)
        return redirect('detail', pk=self.tags.pk)


class TagUpdateView(FormView):
    form_class = TagForms
    template_name = 'tag_update.html'

    def dispatch(self, request, *args, **kwargs):
        self.tag = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Tag, pk=self.kwargs.get('pk'))

    def get_initial(self):
        initial = {
            'summary': self.tag.summary,
            'description': self.tag.description,
            'type': self.tag.type.all(),
            'status': self.tag.status.all(),
        }
        return initial

    def form_valid(self, form):
        types = form.cleaned_data.pop('type')
        statuss = form.cleaned_data.pop('status')
        self.tag.summary = form.cleaned_data.get('summary')
        self.tag.description = form.cleaned_data.get('description')
        self.tag.type.set(types)
        self.tag.status.set(statuss)
        self.tag.save()
        return redirect('detail', pk=self.tag.pk)


class TagDeleteView(View):
    def get(self, request, *args, **kwargs):
        tag = get_object_or_404(Tag, pk=kwargs.get('pk'))
        return render(request, 'tag_delete.html', {'tag': tag})

    def post(self, request, *args, **kwargs):
        tag = get_object_or_404(Tag, pk=kwargs.get('pk'))
        tag.delete()
        return redirect('home')
