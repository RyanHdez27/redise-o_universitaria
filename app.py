from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
