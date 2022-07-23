# 화면을 구성하는 파일

from flask import Blueprint, render_template

from pybo.models import Question

# __init__.py 에서 create_app 함수 안의 hello_pybo 함수를 그대로 옮긴 것.
#  단, @app.route()에서 @bp.route()로 변경

# Blueprint : URL과 함수의 매핑을 관리하기 위해 사용하는 도구(클래스)이다.
bp = Blueprint('main', __name__, url_prefix='/')                         
                                                                
# 여기서 main은 Blueprint의 별칭
# 이 별칭은 나중에 url_for 함수에 사용
# url_prefix 는 함수의 애너테이션 url 앞에 기본값으로 붙일 접두어이다
# url_prefix='/home'으로 입력했다면 호출되는 url은 localhost:5000/home이 된다.

# 이런 식으로 py 파일을 만들어 내용을 추가하면 __init__.py 에서 create_app 함수가 복잡해질 필요가 없다

@bp.route('/hello')
def hello_py():
    return 'Hello, py.'

@bp.route('/')        
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

    # 질문 목록 데이터는 question_list = Question.query.order_by(Question.create_date.desc()) 로 얻을 수 있다
    # order_by(Question.create_date.desc()) 의 의미는 조회된 데이터를 작성일시 기준으로 역순으로 정렬하라는 의미
    # 역순이 아닌 작성일시 순으로 조회하기 위해서는 order_by(Question.create_date.asc()) 또는 asc() 를 생략하여 order_by(Question.create_date)와 같이 사용
