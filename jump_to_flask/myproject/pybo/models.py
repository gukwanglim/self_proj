# 데이터베이스를 처리하는 파일

from pybo import db

# 질문 모델
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# 모델 클래스는 db.Model 클래스를 상속하여 만들어야 한다
# 이 때 사용한 db 객체는 __init__.py 파일에서 생성한 SQLAlchemy 클래스의 객체이다
# Question 모델은 고유 번호(id), 제목(subject), 내용(content), 작성일시(create_date) 속성으로 구성했으며, 각 속성은 db.Column으로 생성했다

# db.Integer는 고유 번호와 같은 숫자값에 사용
# db.String은 제목처럼 글자 수가 제한된 텍스트에 사용
# 글 내용처럼 글자 수를 제한할 수 없는 텍스트는 db.Text를 사용
# 작성일시는 날짜와 시각에 해당하는 db.DateTime을 사용

# 답변 모델
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # question_id 속성은 답변을 질문과 연결하기 위해 추가한 속성
    # 답변은 어떤 질문에 대한 답변인지 알아야 하므로 질문의 id 속성이 필요
    # 모델을 서로 연결할 때에는 위와 같이 db.ForeignKey를 사용해야 한다

    # 데이터베이스에서는 기존 모델과 연결된 속성을 외부 키(foreign key)라고 한다.

    # db.ForeignKey의 첫 번째 파라미터 'question.id'는 question 테이블의 id 컬럼을 의미(question 객체의 속성 id로 착각하지 말자.) 
    # 즉, Answer 모델의 question_id 속성은 question 테이블의 id 컬럼과 연결된다는 뜻

    # db.ForeignKey의 두 번째 파라미터 ondelete는 삭제 연동 설정
    # 즉, ondelete='CASCADE'는 질문을 삭제하면 해당 질문에 달린 답변도 함께 삭제된다는 의미

    # CASCADE 옵션은 데이터베이스 설정이다. 따라서 질문을 데이터베이스 툴에서 쿼리로 삭제할 때만 질문에 달린 답변들이 삭제된다.

    question = db.relationship('Question', backref=db.backref('answer_set'))
    # question 속성은 답변 모델에서 질문 모델을 참조하기 위해 추가
    # db.relationship으로 question 속성을 생성하면 답변 모델에서 연결된 질문 모델의 제목을 answer.question.subject처럼 참조할 수 있다

    # backref 파라미터는 역참조 설정(역참조란 쉽게 말해 질문에서 답변을 거꾸로 참조하는 것을 의미)
    # 한 질문에는 여러 개의 답변이 달릴 수 있는데 역참조는 이 질문에 달린 답변들을 참조할 수 있게 한다
    # 예를 들어 어떤 질문에 해당하는 객체가 a_question이라면 a_question.answer_set와 같은 코드로 해당 질문에 달린 답변들을 참조할 수 있다

    # 더 자세한 내용 참조 https://docs.sqlalchemy.org/en/13/core/type_basics.html

    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)