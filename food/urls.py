"""food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('chefs/',views.chefs,name='chefs'),
    path('contact/',views.contact,name='contact'),
    path('events/',views.events,name='events'),
    path('gallery/',views.gallery,name='gallery'),
    path('menu/',views.menu,name='menu'),
    path('reviews/',views.reviews,name='reviews'), 
    path('specials/',views.specials,name='specials'),
    path('menu/details/<int:id>',views.details,name='details'),
    path('details/<int:id>',views.details,name='details')
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIAFILES_DIRS[0])
