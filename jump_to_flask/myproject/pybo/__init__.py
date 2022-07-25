from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    # config.py 파일에 작성한 항목을 읽기 위해 app.config.from_object(config) 코드를 추가

    # ORM
    db.init_app(app)             # init_app 메서드를 이용해 app에 등록
    migrate.init_app(app, db)   
    from . import models         # 플라스크의 migrate 기능을 인식하기 위해 models를 import 

    # 블루프린트
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app

# 데이터베이스 초기화를 위해 가상환경에서 flask db init 명령으로 데이터베이스를 초기화
# 이렇게 초기화를 실행하면 데이터베이스를 관리하는 초기 파일들을 migrations 파일에 생성
# 데이터베이스를 초기화하는 flask db init 명령은 최초 한 번만 수행하면 된다

# 앞으로 모델을 추가하거나 변경할 때는 flask db migrate 명령과 flask db upgrade 명령만 사용할 것이다

# flask db migrate : 모델을 새로 생성하거나 변경할 때 사용 (실행하면 작업파일이 생성된다.)
# flask db upgrade : 모델의 변경 내용을 실제 데이터베이스에 적용할 때 사용 (위에서 생성된 작업파일을 실행하여 데이터베이스를 변경한다.)

# pybo의 models.py를 import 한 후, 가상환경에서 flask db migrate 실행
# 이 명령을 수행하면 26a0d5f39661_.py처럼 데이터베이스 변경 작업을 위한 리비전 파일이 생성된다(migrations > versions 파일)

# 이어서 flask db upgrade 명령으로 만들어진 리비전 파일을 실행
# 이 과정에서 데이터베이스에 모델 이름과 똑같은 question과 answer라는 이름의 테이블이 생성된다

# 위 과정을 모두 거치면 myproject 디렉터리에 pybo.db 파일이 생성됨

# 이 다음 과정(sqlite 설치, flask shall 사용 등)들은 https://wikidocs.net/81045에 들어가서 확인 