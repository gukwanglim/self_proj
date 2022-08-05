"""config URL Configuration

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
# from django.contrib import admin
from django.urls import path
from .views import Main, UploadFeed
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),          # 장고를 시작하고 127.0.0.1:8000 뒤에 admin을 적으면 admin.site.urls가 실행된다
# ]


# views.py에 Main class를 만든 후, 이곳에 작성하여 연결
urlpatterns = [
    path('', Main.as_view()),
    path('content/upload', UploadFeed.as_view())          # views.py에서 UploadFeed class를 만들었으니 연결
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)     # 사용자들이 업로드한 이미지를 사용할 수 있도록 media에 대한 url도 추가