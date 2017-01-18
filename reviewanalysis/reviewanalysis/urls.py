
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from login.views import *
from django.conf import settings

urlpatterns = [
  #  url(r'^admin/', admin.site.urls),
    url(r'^home/$', index, name='home'),
    url(r'^login/$',login,name='login'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^about/$',about,name='about'),
    url(r'^register/$',register,name='register'),
    url(r'^upload/$',upload,name='upload'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
