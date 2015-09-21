from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('Config.cfg')


@app.route('/')
def index():return "Welcome to to X App"



