
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from final_project.settings import MEDIA_ROOT, MEDIA_URL
from final_project.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    path('products/', include('products.urls')),
    path('providers/', include('providers.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
] + static(MEDIA_URL, document_root = MEDIA_ROOT)


