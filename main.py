from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "xsecretx"
Bootstrap(app)




class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[Length(min=5, max=20), DataRequired()])
    submit = SubmitField(label="Log In")


test_email = "admin@email.com"
test_password = "12345678"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/denied")
def denied():
    return render_template("denied.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        data_email = login_form.email.data
        data_pass = login_form.password.data
        if test_email == data_email and test_password == data_pass:
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
