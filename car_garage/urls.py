"""
URL configuration for car_garage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Admin Customization
admin.site.site_header = "Login to CDT"
admin.site.site_title = "Welcome to CDT Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('', include('visitors_counter.urls')),
]
# if settings.DEBUG:# Only add this when we in debug mode
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# else:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
