# html을 실행할 수 있게 연결하는 파일

from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed

# APIView : 클라이언트와 서버가 데이터를 주고받을 수 있도록 도와주는 역할(여기서는 HTTP 통신)
# 여기서는 HTTP 통신 : 일반적으로 홈페이지를 조회하는 데는 get방식, 특정 작업(?)을 요청할 때는 post방식

class Main(APIView):     # APIView는 djangorestframework라는 패키지를 설치해야 사용할 수 있는 기능
    def get(self, request):    # 'Main 클래스를 get으로 실행했을 때'를 의미,    post를 사용하면 post를 실행했을 때를 의미
        feed_list = Feed.objects.all()
        return render(request, 'config/main.html', context=dict(feed_list=feed_list))     # vs cods에서는 templates 파일을 자동으로 생성하지 않음으로 settings.py에서 templates를 수정해야함
        # render를 사용하면 우리가 만든 html을 브라우저를 통해 보여줄 수 있음
        # Main class를 만들었다면 urls.py에 추가해야 함