from flask import Flask, render_template
from auth_controller import register_user, reset_password, login as login_controller


app = Flask(__name__)
app.secret_key = 'admin8520'

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/portal')
def portal():
    return render_template("portal.html")

@app.route('/login-page')
def login():
    return render_template("login.html")

@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    return login_controller()


@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_user()

@app.route('/reset-password', methods=['GET', 'POST'])
def reset_password_route():
    return reset_password()

if __name__ == "__main__":
    app.run(debug=True)
