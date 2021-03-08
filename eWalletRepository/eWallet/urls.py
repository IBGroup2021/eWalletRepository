"""eWallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from aplicaciones.principal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.Mainmenu, name='main'),
    path('register/', views.RegistrarUsuario, name='register'),
    path('login/', views.LoginUsuario, name='login'),
    path('mainmenu/', views.MenuPrincipal, name='mainmenu'),
    path('logout/', views.logout, name='logout'),
    path('cuenta/', views.cuen, name='cuenta'),
    path('retiro/<str:id>/', views.retirar, name='retiro'),
    path('deposito/<str:id>/', views.depo, name='deposito'),
    path('transferencias/<str:id>/', views.transferencia, name='transferencias'),
    path('veri/<str:id>/', views.verificacion, name = 'veri'),
]
