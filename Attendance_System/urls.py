"""
URL configuration for Attendance_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from .import views,Hod,Staff,Student
from Attendance_System import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base,name='base'),

    # login
    path('',views.user_login,name='user_login'),
    path('dologin/',views.dologin,name='dologin'),
    path('doLogout/',views.doLogout,name='doLogout'),

    # Profile
    path('profile/',views.Profile,name='profile'),

    # HodPanel
    path('Hod/home',Hod.Home,name='hod_home'),
    path('Hod/Student/Add',Hod.add_student,name='add_student'),
    path('Hod/Student/view',Hod.view,name='view'),
    path('Hod/Student/edit/<str:id>',Hod.edit,name='edit'),
    path('Hod/Teacher/Add',Hod.add_teacher,name='add_teacher'),
    path('Hod/Teacher/view_teacher',Hod.view_teacher,name='view_teacher'),

    # StudentPanel
    path('Student/home',Student.home,name='student_home'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
