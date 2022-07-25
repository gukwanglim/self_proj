# flask_self의 프로젝트 환경을 설정(환경변수, 데이터베이스 등)하는 파일

import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLALCHEMY_DATABASE_URI : 데이터베이스 접속 주소
# SQLALCHEMY_TRACK_MODIFICATIONS : SQLAlchemy의 이벤트를 처리하는 옵션

# SQLALCHEMY_DATABASE_URI 설정에 의해 SQLite 데이터베이스가 사용되고 데이터베이스 파일은 프로젝트 홈 디렉터리 바로 밑에 pybo.db 파일로 저장
# 파이썬 기본 패키지에 포함된 SQLite는 주로 소규모 프로젝트에서 사용하는 가벼운 파일을 기반으로 한 데이터베이스

SECRET_KEY = "dev"
# 실제 서비스를 운영할 때에는 "dev"처럼 유추하기 쉬운 문자열을 입력하면 안 된다.