from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    video = FileField('Video', validators=[DataRequired()])
