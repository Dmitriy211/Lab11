"""todo_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasklists/<str:tasklist_name>', views.TaskListDetail.as_view()),
    path('tasklists/', views.TaskListList.as_view()),
    path('tasklists/<str:tasklist_name>/', views.tasklist_tasks),
    path('tasklists/<str:tasklist_name>/<str:task_name>', views.task_detail),
    path('users/', views.UserList.as_view()),
    path('login/', views.login)

]
