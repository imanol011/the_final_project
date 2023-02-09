from django.urls import path 
from providers.views import  ProvidersListView, ProviderCreateView, ProviderDeleteView, ProviderUpdateView

urlpatterns = [
    path('providers-list/', ProvidersListView.as_view(), name='providers_list'),
    path('provider-create/', ProviderCreateView.as_view(), name='providers_create'),
    path('provider-update/<int:pk>/', ProviderUpdateView.as_view(), name='provider_update'),
    path('provider-delete/<int:pk>/', ProviderDeleteView.as_view(), name='provider_delete'),
]