from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from blog.config import Config

db=SQLAlchemy()
bcrypt=Bcrypt()
login_manager= LoginManager()
login_manager.login_view= 'users.login'  #login is function name
login_manager.login_message_category='info'
mail= Mail()




def create_app(confid_class=Config):
    
    app=Flask(__name__)
    app.config.from_object(Config)
    
    from blog.users.routes import users
    from blog.post.routes import posts
    from blog.main.routes import main
    from blog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(errors)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    return app

    
