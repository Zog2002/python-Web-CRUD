

# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from extensions import db, migrate
# from settings import DevConfig
#
#
#
# def create_app():
#     config_object = DevConfig
#     app = Flask(__name__)
#     app.config.from_object(config_object)
#     register_extensions(app)
#
#     @app.errorhandler(404)
#     def page_not_found(error):
#         return render_template('404.html')
#
#     login_manager = LoginManager()
#     login_manager.init_app(app)
#     login_manager.login_view = 'auth.login'
#
#     @login_manager.user_loader
#     def load_user(id):
#         return Customer.query.get(int(id))
#
#     from .views import views
#     from .auth import auth
#     from .admin import admin
#     from .models import Customer, Cart, Product, Order
#
#
#
#     # with app.app_context():
#     #     create_database()
#
#     return app
#
# def register_extensions(app):
#     """
#     Init extension
#     :param app:
#     :return:
#     """
#     db.app = app
#     db.init_app(app)  # SQLAlchemy
#     migrate.init_app(app, db)
#
#
#
