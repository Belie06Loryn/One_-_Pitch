from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, ValidationError, BooleanField, TextAreaField, SelectField, RadioField
from wtforms.validators import Required
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    content = TextAreaField('Post Your Pitch')
    submit = SubmitField('Submit Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField()
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])

class CategoryForm(FlaskForm):
    type_cate = TextAreaField('Category')
    submit = SubmitField()