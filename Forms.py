from flask_wtf import  FlaskForm
from wtforms import  StringField,EmailField,PasswordField,SubmitField
from  wtforms.validators import DataRequired,EqualTo,ValidationError
from Models import User


def check_email_repait(form,field):
    user_email = User.query.filter_by(Email = field.data).first()
    if user_email is not None:
        raise ValidationError("This Email was  enter")




class Reg_Pag(FlaskForm):
    Full_Name = StringField(validators = [DataRequired()])
    Email = EmailField(validators = [DataRequired(), check_email_repait])
    Password = PasswordField(validators = [DataRequired()])
    Confirm_Password = PasswordField(validators = [DataRequired(), EqualTo("Password",message = "Password doesnt match")])

    Submit =  SubmitField("Register")



class Login_Pag(FlaskForm):
    Email = EmailField(validators = [DataRequired()])
    Password = PasswordField(validators = [DataRequired()])

    Submit = SubmitField("Login")

