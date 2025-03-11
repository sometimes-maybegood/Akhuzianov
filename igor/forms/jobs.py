from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    title = StringField('Название работы', validators=[DataRequired()])
    content = StringField("Идентификационный номер руководителя группы", validators=[DataRequired()])
    size = StringField('Размер работы', validators=[DataRequired()])
    collab = StringField("График работы", validators=[DataRequired()])
    is_private = BooleanField("Вы закончили работу")
    submit = SubmitField('Подтвердить')
