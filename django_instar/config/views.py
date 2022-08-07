# html을 실행할 수 있게 연결하는 파일

from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("겟으로 호출")
        return render(request, "config/main.html")

    def post(self, request):
        print("포스트로 호출")
        return render(request, "config/main.html")



# from django.shortcuts import render
# from rest_framework.views import APIView
# from content.models import Feed

# # 프론트엔드에서 업로드한 이미지 및 텍스트 받기
# from rest_framework.response import Response
# import os
# from .settings import MEDIA_ROOT
# from uuid import uuid4


# # APIView : 클라이언트와 서버가 데이터를 주고받을 수 있도록 도와주는 역할(여기서는 HTTP 통신)
# # 여기서는 HTTP 통신 : 일반적으로 홈페이지를 조회하는 데는 get방식, 특정 작업(?)을 요청할 때는 post방식

# class Main(APIView):     # APIView는 djangorestframework라는 패키지를 설치해야 사용할 수 있는 기능
#     def get(self, request):    # 'Main 클래스를 get으로 실행했을 때'를 의미,    post를 사용하면 post를 실행했을 때를 의미
#         feed_list = Feed.objects.all().order_by('-id')
#         return render(request, 'config/main.html', context=dict(feed_list=feed_list))     # vs cods에서는 templates 파일을 자동으로 생성하지 않음으로 settings.py에서 templates를 수정해야함
#         # render를 사용하면 우리가 만든 html을 브라우저를 통해 보여줄 수 있음
#         # Main class를 만들었다면 urls.py에 추가해야 함

# # 업로드 된 정보 받기
# class UploadFeed(APIView):
#     def post(self, request):
#         file = request.FILES['file']                              # file을 처리하기 위해서는 request.FILES를 통해서 파일을 읽어와야 함.
#         uuid_name = uuid4().hex                                   # id를 만드는데 순서대로 만드는 것이 아닌 uuid를 사용하여 값을 랜덤으로 만들어서 고유 id값으로 사용.
#         save_path = os.path.join(MEDIA_ROOT, uuid_name)           # MEDIA_ROOT는 settings.py에서 MEDIA_URL과 MEDIA_ROOT를 만들어서 설정.(사용자가 올리는 파일)
#         with open(save_path, 'wb+') as destination:                         # static은 서버를 돌릴 때 필요한 파일들이고, media는 사용자가 올리는 파일들을 관리하는 곳
#             for chunk in file.chunks():
#                 destination.write(chunk)
#         content = request.data.get('content')
#         image = uuid_name
#         profile_image = request.data.get('profile_image')         # 파일을 제외한 데이터는 request.data.get을 통해 가져올 수 있다
#         user_id = request.data.get('user_id')

#         Feed.objects.create(content=content, image=image, profile_image=profile_image, user_id=user_id, like_count=0)     # request.data.get을 통해 가져온 데이터를 가지고 Feed.objects.create를 통해 새로운 Feed를 만들 수 있습니다.

#         return Response(status=200)      #클라이언트에게 status=200인 응답(Response)을 줍니다.