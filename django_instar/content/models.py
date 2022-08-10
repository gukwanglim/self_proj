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


class Like(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_like = models.BooleanField(default=True)             # 여기서 BooleanField를 사용하지만 Mysql에서는 Boolean이 없기 때문에 tinyint로 들어가게 되고 tinyint(1)은 숫자가 들어갈 경우 True라고 표현할 수 있다.
                                                            # tinyint(1)은 숫자가 들어갈 경우 True라고 표현할 수 있다. 또한, 0이 들어가게 된다면 False를 뜻하게 된다.

class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    reply_content = models.TextField()


class Bookmark(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_marked = models.BooleanField(default=True)