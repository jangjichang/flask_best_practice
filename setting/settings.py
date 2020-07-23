from flask import Flask

def create_app(name=__name__):
    app = Flask(name)
    app.config.from_pyfile('setting/debug_env.cfg')

    print(app.config)
    return app
