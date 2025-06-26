"""
URL configuration for project_files project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app1.views import ItemOneViewSet,movie1_list_html
from app2.views import MovieViewSet,movie_list_html
from app1.views import itemone_update_html, itemone_delete_html

router = routers.DefaultRouter()
router.register(r'app1', ItemOneViewSet, basename='app1')
router.register(r'app2', MovieViewSet,  basename='app2')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  #for the apps
    path('api-auth/', include('rest_framework.urls')),
    path('movies/html/', movie_list_html, name = 'movie-list-html'),
    path('items/html/', movie1_list_html, name = 'movie1-list-html')
]
urlpatterns += [
    path('items/html/<int:pk>/edit/',   itemone_update_html,  name='itemone-update-html'),
    path('items/html/<int:pk>/delete/', itemone_delete_html,  name='itemone-delete-html'),
]