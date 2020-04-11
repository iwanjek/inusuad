from flask import Flask
from flask_bootstrap import Bootstrap
import configparser

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello world'
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('setup.cfg')

    app.run(debug=True, port=80, host='0.0.0.0')