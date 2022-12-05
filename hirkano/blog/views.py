from django.views.generic.base import TemplateView
from .models import (
    SlideShow,
    Service,
    Selected_Title,
    Activity,
    Person,
    Blog,
    Contant_Us,
    Message,
)
from .form import(
    MessageForm,
)


class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'slide_showes' : SlideShow.objects.all(),
            'services' : Service.objects.all(),
            'selected_title': Selected_Title.objects.all(),
            'activites': Activity.objects.all(),
            'person': Person.objects.all(),
            'blog':Blog.objects.all(),
            'contant_us':Contant_Us.objects.all(),
            'message':Message.objects.all(),
            'messageForm':MessageForm(request.POST)
        })

        return context
