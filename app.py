from flask import Flask, render_template, url_for, current_app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisisasecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from routes import bp as routes_bp
    app.register_blueprint(routes_bp)
    return app






if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
