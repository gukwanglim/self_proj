from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question
from pybo.forms import QuestionForm, AnswerForm          # forms.py에서 만든 QuestionsForm 클래스를 import한다

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form) 

# question_list.html에서 만들어진 질문 등록 버튼에 연동
@bp.route('/create/', methods=('GET', 'POST'))  # question_form.html에서 질문 등록 버튼의 method는 post 방식을 사용한다 그러므로 get과 post 방식을 모두 처리할 수 있게 해준다
def create():
    form = QuestionForm()
    # question_form.html 템플릿에 전달하는 QuestionForm의 객체(form)는 템플릿에서 라벨이나 입력폼 등을 만들때 필요하다.
    # question_form.html을 만들어야한다

    # 이후 템플릿에 전송한 폼 데이터를 저장하는 코드를 작성해야한다(if 구문 추가)
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    # if 문의 request.method는 create 함수로 요청된 전송 방식을 의미
    # form.validate_on_submit 함수는 전송된 폼 데이터의 정합성을 점검
    # 즉, QuestionForm 클래스의 각 속성에 지정한 DataRequired() 같은 점검 항목에 이상이 없는지 확인한다

    # 즉, 위 코드에 추가한 내용(if 문)은 POST 요청이고 폼 데이터에 이상이 없을 경우 질문을 저장한 뒤 main.index 페이지로 이동하라는 내용

    # 코드를 보면 폼으로부터 전달받은 "제목"에 해당하는 데이터는 form.subject.data로 얻고 있다. form.content.data도 마찬가지이다.

    # 코드의 핵심은 데이터 전송 방식이 POST인지 GET인지에 따라서 달리 처리하는 부분이다.
    # 질문 목록에서 <질문 등록하기> 버튼을 누르거나 질문 등록 화면에서 <저장하기> 버튼을 누르면 똑같이 localhost:5000/question/create/ 페이지를 요청하므로 create 함수가 이 요청을 받는다
    # 다만 create 함수에서 요청 방식을 구분해서 처리한다
    # 즉, <질문 등록하기> 버튼을 누르는 것은 GET 방식 요청이므로 질문 등록 화면을 보여 주고
    # <저장하기>버튼을 누르면 POST 방식 요청이므로 데이터베이스에 질문을 저장한다.

    # 그런데 여기까지 작성하고 <저장하기> 버튼을 눌러도 제대로 동작하지 않는다.(CSRF 문제를 해결해야 저장이 가능하다)
    
    return render_template('question/question_form.html', form=form)
