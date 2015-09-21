from flask import Flask
from Model import  db

app = Flask(__name__)
app.config.from_pyfile('Config.cfg')

#Plug SQLAlchemy to your application
db.init_app(app)



@app.route('/')
def index():return "Welcome to to X App"

@app.route('/install')
def installer():
  db.drop_all()
  db.create_all()
  return '{"Success":"True","Message":"Application have been initialized successfully do not forget to make this secure or disable it after the installation"}',200

