from django.views.generic import TemplateView
from service.models import Service


class ServiceView(TemplateView):
    template_name = 'services/services.html'
    queryset = Service.objects.all()


class ContactView(TemplateView):
    template_name = 'contact/contact.html'
