# from flask import Flask
# from app.api.first import lantu
#
# app = Flask(__name__)
# app.register_blueprint(lantu, url_prefix='/test')
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'

from flask_script import Manager
from app import init_app


app = init_app()
mgr = Manager(app)

if __name__ == '__main__':
    mgr.run()