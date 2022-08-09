from django.db import models

# Create your models here.

# class Feed(models.Model):
#     content = models.TextField()
#     image = models.TextField()
#     profile_image = models.TextField()
#     user_id = models.TextField()
#     like_count = models.IntegerField()

class Feed(models.Model):
    content = models.TextField()              # 글내용
    image = models.TextField()                # 피드 이미지
    email = models.EmailField(default='')     # 글쓴이