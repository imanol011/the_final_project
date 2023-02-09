from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from providers.models import Provider


class ProvidersListView(LoginRequiredMixin, ListView):
    model = Provider
    template_name = 'providers/providers-list.html'
    queryset = Provider.objects.filter(is_active = True)

class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'providers/providers-create.html'
    fields = '__all__'
    success_url = '/providers/providers-list/'

class ProviderUpdateView(UpdateView):
    model = Provider
    template_name = 'providers/providers-update.html'
    fields = '__all__'
    success_url = '/providers/providers-list/'

class ProviderDeleteView(DeleteView):
    model = Provider
    template_name = 'providers/providers-delete.html'
    success_url = '/providers/providers-list/'

