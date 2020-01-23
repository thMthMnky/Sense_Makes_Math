from flask import Flask, request
from flask_caching import Cache
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
import logging

# from flask_moment import Moment
# from flask_babel import Babel, lazy_gettext as _l
# from flask_pagedown import PageDown
# import os
from datetime import datetime as dt
# from elasticsearch import Elasticsearch
# from redis import Redis

from config import config
db = SQLAlchemy()
cache = Cache()
mail = Mail()
bootstrap = Bootstrap()
migrate = Migrate()
login = LoginManager()
# login.login_view = 'auth.login'
# login.login_message = 'Please log in to access this page.'
# moment = Moment()
# babel = Babel()
# pagedown = PageDown()


def register_extensions(app):
    cache.init_app(app=app, config={'CACHE_TYPE': app.config['CACHE_TYPE']})
    db.init_app(app)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)
    # moment.init_app(app)
    # babel.init_app(app)
    # pagedown.init_app(app)
    # logs.init_app(app)
    # app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
    #     if app.config['ELASTICSEARCH_URL'] else None
    # app.redis = Redis.from_url(app.config['REDIS_URL'])
    # app.task_queue = rq.Queue('microblog-tasks', connection=app.redis)

    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify()
        sslify.init_app(app)
    return None


def register_blueprints(app):
    from .main import main_bp
    app.register_blueprint(main_bp)

    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    from .errors import errors_bp
    app.register_blueprint(errors_bp)

    return None


def create_app(config_name=None):
    app = Flask(__name__)
    config[config_name].init_app(app)
    app.config.from_object(config[config_name])

    with app.app_context():

        # @app.before_request
        # def before_request():
        #     if 'logged_in' not in session and request.endpoint != 'login':
        #         return redirect(url_for('login'))

        @app.after_request
        def after_request(response):
            """ Logging after every request. """
            app.logger.info(
                "%s [%s] %s %s %s %s %s %s %s",
                request.remote_addr,
                dt.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
                request.method,
                request.path,
                request.scheme,
                response.status,
                response.content_length,
                request.referrer,
                request.user_agent)
            return response

        register_extensions(app)
        register_blueprints(app)

        db.create_all()

        app.logger.setLevel(logging.INFO)
        app.logger.info('Starting UP: Sense Makes Math')
        return app
