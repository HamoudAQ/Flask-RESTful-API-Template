from flask import Flask,jsonify
from Model import  db
from flask.ext.restful import Api
from resources.User import RU_User

app = Flask(__name__)
app.config.from_pyfile('Config.cfg')

#Plug SQLAlchemy to your application
db.init_app(app)

#Plug restful to your application
restful_api = Api(app)



@app.route('/')
def index():return "Welcome to to X App"

@app.route('/install')
def installer():
  db.drop_all()
  db.create_all()
  return jsonify({"Success":"True","Message":"Application have been initialized successfully do not forget to make this secure or disable it after the installation"})



#API Calls definition 
restful_api.add_resource(RU_User,'/API/User')#GET for Read,PUT for update
