from uuid import uuid4
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed                          # , Reply, Like, Bookmark
from user.models import User
import os
from config.settings import MEDIA_ROOT

# Create your views here.
class Main(APIView):
    def get(self, request):
        print("겟으로 호출")
        feed_object_list = Feed.objects.all().order_by('-id')                # select * from contnet_feed;     사람들이 올린 피드를 역순으로 화면에 띄우기 위해 필요한 feed_object_list
        # print('데이터베이스 안에 들어있는 내용 : ', feed_list)

        feed_list = []                                                       # content/models.py에서 Feed 테이블을 변경했기 때문에 여러 테이블에서 피드에 필요한 내용들을 뽑아내 리스크로 만들기.

        for feed in feed_object_list:
            user = User.objects.filter(email=feed.email).first()
            # reply_object_list = Reply.objects.filter(feed_id=feed.id)
            # reply_list = []
            # for reply in reply_object_list:
                # user = User.objects.filter(email=reply.email).first()
                # reply_list.append(dict(reply_content=reply.reply_content,
                                    #    nickname=user.nickname))
            # like_count=Like.objects.filter(feed_id=feed.id, is_like=True).count()
            # is_liked=Like.objects.filter(feed_id=feed.id, email=email, is_like=True).exists()
            # is_marked=Bookmark.objects.filter(feed_id=feed.id, email=email, is_marked=True).exists()
            feed_list.append(dict(id=feed.id,
                                  image=feed.image,
                                  content=feed.content,
                                #   like_count=like_count,
                                  profile_image=user.profile_image,
                                  nickname=user.nickname,
                                #   reply_list=reply_list,
                                #   is_liked=is_liked,
                                #   is_marked=is_marked
                                  ))

        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()

        return render(request, "config/main.html", context=dict(feed_list=feed_list, user=user))

# # 업로드 된 정보 받기(API 만들기)
class UploadFeed(APIView):
    def post(self, request):
        # 파일 불러오기
        file = request.FILES['file']                              # file을 처리하기 위해서는 request.FILES를 통해서 파일을 읽어와야 함.(파일 불러오기)
        uuid_name = uuid4().hex                                   # id를 만드는데 순서대로 만드는 것이 아닌 uuid를 사용하여 값을 랜덤으로 만들어서 고유 id값으로 사용.(이미지 이름이 한글, 영어, 특수문자 등이 섞여 있을 수 있으므로 유효 아이디를 생성)
        save_path = os.path.join(MEDIA_ROOT, uuid_name)           # MEDIA_ROOT는 settings.py에서 MEDIA_URL과 MEDIA_ROOT를 만들어서 설정.(사용자가 올리는 파일), (즉, 'media/유효아이디'의 형태로 저장하겠다.)
        
        with open(save_path, 'wb+') as destination:                         # static은 서버를 돌릴 때 필요한 파일들이고, media는 사용자가 올리는 파일들을 관리하는 곳
            for chunk in file.chunks():
                destination.write(chunk)

        content = request.data.get('content')
        image = uuid_name
        email = request.session.get('email', None)      # 아래 두 정보는 필요가 없지만 이메일을 필요해진다.(물론 로그인 한 상태이므로 이것도 그렇게 필요하진 않다.)


           # profile_image와 user_id는 글을 올릴 때 따로 들고 있다가 올릴 필요가 없다(로그인을 해야만 글을 올릴 수 있는데 그렇게 된다면 로그인을 한 정보를 들고와 사용하면 되기 때문이다.)
        # profile_image = request.data.get('profile_image')         # 파일을 제외한 데이터는 request.data.get을 통해 가져올 수 있다
        # user_id = request.data.get('user_id')

        Feed.objects.create(content=content, image=image, email=email)     # request.data.get을 통해 가져온 데이터를 가지고 Feed.objects.create를 통해 새로운 Feed를 만들 수 있습니다.

        return Response(status=200)      #클라이언트에게 status=200인 응답(Response)을 줍니다.(API)


class Profile(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()

        # feed_list = Feed.objects.filter(email=email)

        return render(request, 'content/profile.html', context=dict(# feed_list=feed_list,
                                                                    # like_feed_list=like_feed_list,
                                                                    # bookmark_feed_list=bookmark_feed_list,
                                                                    user=user))






# class Main(APIView):
#     def get(self, request):
#         email = request.session.get('email', None)

#         if email is None:
#             return render(request, "user/login.html")

#         user = User.objects.filter(email=email).first()

#         if user is None:
#             return render(request, "user/login.html")

#         feed_object_list = Feed.objects.all().order_by('-id')  # select  * from content_feed;
#         feed_list = []

#         for feed in feed_object_list:
#             user = User.objects.filter(email=feed.email).first()
#             reply_object_list = Reply.objects.filter(feed_id=feed.id)
#             reply_list = []
#             for reply in reply_object_list:
#                 user = User.objects.filter(email=reply.email).first()
#                 reply_list.append(dict(reply_content=reply.reply_content,
#                                        nickname=user.nickname))
#             like_count=Like.objects.filter(feed_id=feed.id, is_like=True).count()
#             is_liked=Like.objects.filter(feed_id=feed.id, email=email, is_like=True).exists()
#             is_marked=Bookmark.objects.filter(feed_id=feed.id, email=email, is_marked=True).exists()
#             feed_list.append(dict(id=feed.id,
#                                   image=feed.image,
#                                   content=feed.content,
#                                   like_count=like_count,
#                                   profile_image=user.profile_image,
#                                   nickname=user.nickname,
#                                   reply_list=reply_list,
#                                   is_liked=is_liked,
#                                   is_marked=is_marked
#                                   ))


#         return render(request, "config/main.html", context=dict(feeds=feed_list, user=user))


# class UploadFeed(APIView):
#     def post(self, request):

#         # 일단 파일 불러와
#         file = request.FILES['file']

#         uuid_name = uuid4().hex
#         save_path = os.path.join(MEDIA_ROOT, uuid_name)

#         with open(save_path, 'wb+') as destination:
#             for chunk in file.chunks():
#                 destination.write(chunk)

#         asdf = uuid_name
#         content123 = request.data.get('content')
#         email = request.session.get('email', None)

#         Feed.objects.create(image=asdf, content=content123, email=email)

#         return Response(status=200)


# class Profile(APIView):
#     def get(self, request):
#         email = request.session.get('email', None)

#         if email is None:
#             return render(request, "user/login.html")

#         user = User.objects.filter(email=email).first()

#         if user is None:
#             return render(request, "user/login.html")

#         feed_list = Feed.objects.filter(email=email)
#         like_list = list(Like.objects.filter(email=email, is_like=True).values_list('feed_id', flat=True))
#         like_feed_list = Feed.objects.filter(id__in=like_list)
#         bookmark_list = list(Bookmark.objects.filter(email=email, is_marked=True).values_list('feed_id', flat=True))
#         bookmark_feed_list = Feed.objects.filter(id__in=bookmark_list)
#         return render(request, 'content/profile.html', context=dict(feed_list=feed_list,
#                                                                     like_feed_list=like_feed_list,
#                                                                     bookmark_feed_list=bookmark_feed_list,
#                                                                     user=user))


# class UploadReply(APIView):
#     def post(self, request):
#         feed_id = request.data.get('feed_id', None)
#         reply_content = request.data.get('reply_content', None)
#         email = request.session.get('email', None)

#         Reply.objects.create(feed_id=feed_id, reply_content=reply_content, email=email)

#         return Response(status=200)


# class ToggleLike(APIView):
#     def post(self, request):
#         feed_id = request.data.get('feed_id', None)
#         favorite_text = request.data.get('favorite_text', True)

#         if favorite_text == 'favorite_border':
#             is_like = True
#         else:
#             is_like = False
#         email = request.session.get('email', None)

#         like = Like.objects.filter(feed_id=feed_id, email=email).first()

#         if like:
#             like.is_like = is_like
#             like.save()
#         else:
#             Like.objects.create(feed_id=feed_id, is_like=is_like, email=email)

#         return Response(status=200)


# class ToggleBookmark(APIView):
#     def post(self, request):
#         feed_id = request.data.get('feed_id', None)
#         bookmark_text = request.data.get('bookmark_text', True)
#         print(bookmark_text)
#         if bookmark_text == 'bookmark_border':
#             is_marked = True
#         else:
#             is_marked = False
#         email = request.session.get('email', None)

#         bookmark = Bookmark.objects.filter(feed_id=feed_id, email=email).first()

#         if bookmark:
#             bookmark.is_marked = is_marked
#             bookmark.save()
#         else:
#             Bookmark.objects.create(feed_id=feed_id, is_marked=is_marked, email=email)

#         return Response(status=200)