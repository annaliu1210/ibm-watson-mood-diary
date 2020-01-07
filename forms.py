from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class DiaryEntry(FlaskForm):
    text = TextAreaField('Diary Entry', validators=[DataRequired()])
    submit = SubmitField('Submit')
