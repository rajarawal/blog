"""blog_project URL Configuration

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
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.post_list_view),
    path('tag/<str:tag_slug>/',views.post_list_view , name = 'post_list_by_tag'),
    #path('' , views.PostListView.as_view()),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail_view , name ='post_detail'),
    path('<int:id>/share',views.send_mail_view),
]
# EMAIL_HOST= 'smtp.gmail.com'
# EMAIL_PORT= 587
# EMAIL_HOST_USER= Username for SMTP Server
# EMAIL_HOST_PASSWORD=Password for SMTP Server
# EMAIL_USE_TLS= True
