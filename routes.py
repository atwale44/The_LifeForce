from flask import Blueprint, current_app as app, g
from app import db
from models import User

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    with g.app.app_context():
        db.create_all()
    return 'Hello, Flask with SQlite!'

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')