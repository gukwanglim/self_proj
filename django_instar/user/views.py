import os
from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password
from config.settings import MEDIA_ROOT


class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html")

    def post(self, request):
        # TODO 회원가입                 # 프로필 이미지는 회원가입 하고 나서 바꿀 수 있기 때문에 넣지 않는다.
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),           # 패스워드는 해시 암호화를 하여 보안.
                            profile_image="image.gif")        # 프로필 이미지는 아직 사용자가 올리지 않았으므로 기본 이미지로 저장

        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        # TODO 로그인
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))

        if user.check_password(password):                                               # 만약 패스워드가 맞다면 True, 틀리면 False를 반환.
            # TODO 로그인을 했다. 세션 or 쿠키
            request.session['email'] = email                                            # 로그인을 성공했다면 session에 저장하여 로그인한 아이디의 정보를 불러오기 위해
            return Response(status=200)                                                 # (session에 저장하면 Login에만 적용되는 것이 아닌 Main등의 class가 실행되는 순간에도 정보를 가져올 수 있게 된다.)
        else:
            return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))


class LogOut(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, "user/login.html")


class UploadProfile(APIView):
    def post(self, request):

        # 일단 파일 불러와
        file = request.FILES['file']
        email = request.data.get('email')

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        profile_image = uuid_name

        user = User.objects.filter(email=email).first()

        user.profile_image = profile_image
        user.save()                                # 파일을 만드는 것이 아닌 수정하는 것이므로 create가 아닌 save()를 사용.

        return Response(status=200)
