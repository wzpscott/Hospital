"""Hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from HMIS import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start),

    path('login/', views.login),
    path('logout/', views.logout),

    path('patientLogin/', views.patientLogin),
    path('patientRegister/', views.patientRegister),
    path('patientIndex/', views.patientIndex),
    path('patientIndex/info', views.patientInfo),
    path('patientIndex/registration', views.registration),

    path('doctorLogin/', views.doctorLogin),
    path('doctorRegister/', views.doctorRegister),
    path('doctorIndex/', views.doctorIndex),
    path('doctorIndex/info', views.doctorInfo),
    path('doctorIndex/registrationRecord', views.registrationRecord),

    path('doctorIndex/treatment', views.treatment),
]
