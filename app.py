from flask import Flask, render_template
from auth_controller import register_user

app = Flask(__name__)
app.secret_key = 'admin8520'

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/portal')
def portal():
    return render_template("portal.html")
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/ingresar')
def ingresar():
    return render_template("login_ll.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_user()

if __name__ == "__main__":
    app.run(debug=True)
