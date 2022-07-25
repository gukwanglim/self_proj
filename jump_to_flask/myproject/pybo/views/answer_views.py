from datetime import datetime

from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import AnswerForm
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
# 답변 등록은 POST요청만 있으므로 GET, POST 분기처리는 필요없다.
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now())
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))

    # content = request.form['content']                                # POST 폼 방식으로 전송된 데이터 항목 중 name 속성이 content인 값을 의미
    # answer = Answer(content=content, create_date=datetime.now())
    # question.answer_set.append(answer)                               # "질문에 달린 답변들"을 의미
    # db.session.commit()
    # return redirect(url_for('question.detail', question_id=question_id))

    return render_template('question/question_detail.html', question=question, form=form)

# @bp.route의 methods 속성에는 'POST'를 지정했다. 
# 답변을 저장하는 질문 상세 템플릿의 form 엘리먼트가 POST 방식이므로 같은 값을 지정해야 한다. 
# 만약 @bp.route에 똑같은 폼 방식을 지정하지 않으면 오류가 발생하므로 주의하자.


    # answer = Answer(question=question, content=content, create_date=datetime.now())
    # db.session.add(answer)
    # 이런 식으로 답변을 저장할수도 있다