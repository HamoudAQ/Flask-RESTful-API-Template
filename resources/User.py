from flask.ext.restful import Resource
from flask import g,jsonify
from Model import Users,db

from common.Auth import Users as Users_login




class RU_User(Resource):#Read and Update
    decorators = [Users_login.auth.login_required]
    def get(self):#view display_name and phone
        Response = jsonify({"Displayed_Name":g.user.Displayed_Name,"Phone":g.user.Phone})
        Response.status_code=200
        return Response

    def put(self):#update display_name only
        try:
            input = UserInformation.parse_args()
            if len(input['DNAME'])>0:
                User_record = Users.query.filter_by(id=g.user.id).first()
                User_record.Displayed_Name=input['DNAME']
                db.session.add(User_record)
                db.session.commit()

                Response = jsonify({"Success":"True","Message":"User Displayed name have been updated successfully"})
                Response.status_code=200
                return Response

        except Exception,r:
            Response = jsonify({"Success":"False","Message":str(r)})
            Response.status_code=400
            return Response

