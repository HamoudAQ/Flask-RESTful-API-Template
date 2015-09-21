from flask.ext.httpauth import HTTPBasicAuth
from flask import  g
from Model import Client

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):#we consider User phone as username 
    user = Client.query.filter_by(Phone = username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True
