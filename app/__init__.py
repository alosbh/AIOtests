from flask import Flask

def create_app():
    app = Flask(__name__)    

    hostfile = open('/usr/src/app/etc/hostname')
    for line in hostfile:
        print (line)

    @app.route('/')
    def index():
        return 'Hello, world'

    return app

# export FLASK_APP=app
# python -m flask run --host=0.0.0.0 --port=8888
