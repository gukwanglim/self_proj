from urllib.request import AbstractBasicAuthHandler
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    """
        유저 프로파일 사진
        유저 닉네임     -> 화면에 표기되는 이름
        유저 이름       -> 실제 사용자 이름
        유저 이메일주소 -> 회원가입할때 사용하는 아이디
        유저 비밀번호 -> 디폴트 쓰자(장고의 user 기능을 상속받으면 비밀번호는 디폴트값으로 들어간다.)
    """
    profile_image = models.TextField()  # 프로필 이미지
    nickname = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname'

    class Meta:               # 테이블명을 '파일명_클래스명'(ex - content_feed)로 만드는 것이 아닌 직접 정하는 것.
        db_table = "User"