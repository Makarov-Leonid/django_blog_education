from django.shortcuts import get_object_or_404, render
from django.views import View

from blog.models import Post


class ObjectDetailMixin(View):
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})