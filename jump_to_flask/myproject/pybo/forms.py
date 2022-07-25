# 서버로 전송된 폼을 처리하는 파일

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

# 질문 등록시 사용할 QuestionForm
class QuestionForm(FlaskForm):
    # QuestionForm과 같은 플라스크의 폼은 FlaskForm 클래스를 상속하여 만들어야 한다
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])     # 글자수의 제한이 있는 "제목"의 경우 StringField를 사용
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])   # 글자수의 제한이 없는 "내용"은 TextAreaField를 사용
# validators는 검증을 위해 사용되는 도구로 필수 항목인지를 체크하는 DataRequired, 이메일인지를 체크하는 Email, 길이를 체크하는 Length등이 있다
# 예를들어 필수값이면서 이메일이어야 하면 validators=[DataRequired(), Email()] 과 같이 사용할 수 있다

# 이렇게 forms 항목을 작성한 다음 question_views.py에서 라우팅 함수 create를 작성

# DataRequired에 한글 메시지를 설정 -> 한글로 오류가 작성되게 만든다

class AnswerForm(FlaskForm):
    content = TextAreaField('답변 내용', validators=[DataRequired('답변 내용은 필수입력 항목입니다.')])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])

# 로그인시 사용할 UserLoginForm
class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])