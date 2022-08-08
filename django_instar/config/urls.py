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
from django.contrib import admin
from django.urls import path, include
# from .views import Sub
from content.views import Main
from .settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),          # 장고를 시작하고 127.0.0.1:8000 뒤에 admin을 적으면 admin.site.urls가 실행된다
# ]


# views.py에 Main class를 만든 후, 이곳에 작성하여 연결
urlpatterns = [
    path('', Main.as_view()),                                       # content/views.py에서 Main class를 만들었으니 연결.
    # path('content/upload', UploadFeed.as_view())                   # script.js에서 '공유하기' 버튼 ajax를 설정할 때, url: "contnet/upload"로 설정하고 content/views.py에서 UploadFeed를 만들었기에 연결.
    path('content/', include('content.urls')),                              # 이런 식으로 include를 사용하면 config/urls.py가 길어지는 것을 방지할 수 있다.(content/urls.py에 적힌 내용을 가져와서 사용.)
    path('user/', include('user.urls')),
    path('user/', include('user.urls'))
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)     # 사용자들이 업로드한 이미지를 사용할 수 있도록 media에 대한 url도 추가. media에 이미지 파일을 저장하면 그것을 조회할 수 있게 만들어주는 코드.