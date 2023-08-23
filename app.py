from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def welcome():
    """Display a simple welcome message"""

    html = "<html><body><h1>Welcome</h1></body></html>"
    return html


@app.get('/welcome/home')
def welcome_home():
    """Display a simple "welcome home" message"""

    html = "<html><body><h1>Welcome Home</h1></body></html>"
    return html


@app.get('/welcome/back')
def welcome_back():
    """Display a simple "welcome back" message"""

    html = "<html><body><h1>Welcome Back!</h1></body></html>"
    return html