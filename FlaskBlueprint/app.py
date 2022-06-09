# from flask import Flask
# from app.api.first import lantu
#
# app = Flask(__name__)
# app.register_blueprint(lantu, url_prefix='/test')
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'

from app import init_app


app = init_app()

if __name__ == '__main__':
    app.run()
