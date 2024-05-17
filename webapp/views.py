from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
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


class TagCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TagForms()
        context = {'form': form}
        return render(request, 'tag_create.html', context)

    def post(self, request, *args, **kwargs):
        form = TagForms(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('type')
            statuss = form.cleaned_data.pop('status')
            tags = Tag.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description'),

            )
            tags.type.set(types)
            tags.status.set(statuss)
            return redirect('home')
        else:
            context = {'form': form}
            return render(request, 'tag_create.html', context)


class TagUpdateView(TemplateView):
    template_name = 'tag_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = get_object_or_404(Tag, pk=kwargs.get('pk'))
        form = TagForms(initial={
            'summary': tag.summary,
            'description': tag.description,
            'type': tag.type.all(),
            'status': tag.status.all(),
        })
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        tag = get_object_or_404(Tag, pk=kwargs.get('pk'))
        form = TagForms(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('type')
            statuss = form.cleaned_data.pop('status')
            tag.summary = form.cleaned_data.get('summary')
            tag.description = form.cleaned_data.get('description')
            tag.type.set(types)
            tag.status.set(statuss)
            tag.save()
            return redirect('detail', pk=tag.pk)
        else:
            context = {'form': form}
            return render(request, 'tag_update.html', context)


class TagDeleteView(View):
    def get(self, request, *args, **kwargs):
        tag = get_object_or_404(Tag, pk=kwargs.get('pk'))
        return render(request, 'tag_delete.html', {'tag': tag})

    def post(self, request, *args, **kwargs):
        tag = get_object_or_404(Tag, pk=kwargs.get('pk'))
        tag.delete()
        return redirect('home')
