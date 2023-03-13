from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect






class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    bedrooms = IntegerField('No. of Rooms', validators=[DataRequired()])
    bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    description = TextAreaField('Description',validators=[DataRequired()])
    type = SelectField('Type', choices=[('house', 'House'), ('apartment', 'Apartment')], validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired()])
    submit = SubmitField('Add Property')
