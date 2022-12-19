"""blog URL Configuration

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
from apps.post.views import home, quienes_somos, proyectos, servicios, publicaciones, areas_de_estudio, crear_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('quienes-somos/', quienes_somos),
    path('proyectos/', proyectos),
    path('servicios/', servicios),
    path('publicaciones/', publicaciones),
    path('areas-de-estudio/', areas_de_estudio),
    path('crear-post', crear_post),
]