from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from HMS.models import Userstore


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=8)])
    password = StringField("Password", validators=[DataRequired(), Length(min=1, max=15)])
    submit = SubmitField("Login")

class UpdateForm(FlaskForm):
    ws_ssn = StringField("SSN")
    ws_pat_id = StringField("Patient_id")
    ws_pat_name = StringField("Name",validators=[Length(max=50)])
    ws_adrs = StringField("Address", validators=[Length(max=255)])
    ws_state =StringField("State", validators=[Length(max=50)])
    ws_city = StringField("City", validators=[Length(max=50)])
    ws_age = IntegerField("Age")
    ws_doj = DateField("Date_of_joining")
    ws_rtype = StringField("Room_type")
    submit = SubmitField("Update")

class CreateForm(FlaskForm):
    ws_ssn = StringField("SSN")
    ws_pat_id = StringField("Patient_id")
    ws_pat_name = StringField("Name",validators=[Length(max=50)])
    ws_adrs = StringField("Address", validators=[Length(max=255)])
    ws_state =StringField("State", validators=[Length(max=50)])
    ws_city = StringField("City", validators=[Length(max=50)])
    ws_age = IntegerField("Age")
    ws_doj = DateField("Date_of_joining")
    ws_rtype = SelectField("Room_type", choices=[("General Ward","General Ward"),("Semi sharing","Semi sharing"),("Single room","Single room")])
    ws_status = StringField("Status")
    submit = SubmitField("Add")


