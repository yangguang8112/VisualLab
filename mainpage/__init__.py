import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import database
    database.init_app(app)

    from . import mainp
    app.register_blueprint(mainp.bp)
    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/ztron_upload', endpoint='ztron_upload')
    app.add_url_rule('/api_eg', endpoint='api_show')
    app.add_url_rule('/pipe_upload', endpoint='pipe_upload')

    return app