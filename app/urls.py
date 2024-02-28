"""
URL configuration for kittens_django project.

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
from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.KittenListView.as_view(), name='index'),
    path('kitten/<int:pk>', view=views.KittenDetailView.as_view(), name='kitten-detail'),
    path('kitten/create', view=views.KittenCreate.as_view(), name='kitten-create'),
    path('kitten/<int:pk>/update/', view=views.KittenUpdate.as_view(), name='kitten-update'),
    path('kitten/<int:pk>/delete/', view=views.KittenDelete.as_view(), name='kitten-delete'),
]
