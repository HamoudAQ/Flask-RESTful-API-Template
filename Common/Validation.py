from flask_restful import reqparse


#to get input from http header if data sent via post/put/delete
UserInformation = reqparse.RequestParser()
UserInformation.add_argument("DNAME",type=str,help="User Displayed name")
