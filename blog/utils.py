from pprint import pprint

from django.shortcuts import render, get_object_or_404, redirect


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context=({self.model.__name__.lower(): obj, 'admin_object': obj}))


class ObjectCreateMixin:
    form = None
    template = None

    def get(self, request):
        pprint(dir(request))
        pprint(dir(request.user))
        obj = self.form()
        return render(request, self.template, context=({'form': obj}))

    def post(self, request):
        bound_form = self.form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    template = None
    model_form = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'bound_form': bound_form})

    def post(self, request, slug):
        obj = self.model.objects.get(slug=slug)
        bound_form = self.model_form(request.POST, instance=obj)
        if bound_form.is_valid():
            updated_tag = bound_form.save()
            return redirect(updated_tag)
        return render(request, 'blog/tag_update.html',
                      context={self.model.__name__.lower(): obj, 'bound_form': bound_form})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug=slug)
        obj.delete()
        return redirect(self.redirect_url)
