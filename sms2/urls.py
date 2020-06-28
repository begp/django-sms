from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('user.urls')),
    path('students/', include('stumgmt.urls')),
    path('academics/', include('academy.urls')),
    path('employee/', include('staff_mgmt.urls')),
    path('', TemplateView.as_view(template_name='home.html')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
