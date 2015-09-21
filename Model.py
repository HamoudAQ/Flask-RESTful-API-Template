from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()

#Example of entity (table)
class Users(db.Model):
    __tablename__  = 'Users'
    id             = db.Column(db.Integer, primary_key=True)
    Displayed_Name = db.Column(db.String(80,collation='utf8_unicode_ci'),nullable=False)
    Phone          = db.Column(db.String(12), unique=True,nullable=False)
    Password       = db.Column(db.String(5), nullable=False)

    def __init__(self, displayed_name, phone,password):
        self.Displayed_Name = displayed_name
        self.Phone          = phone
        self.password       = password
    def __repr__(self):
        return '<%i,%r,%r>' % (self.id,self.Displayed_name,self.Phone)
    def verify_password(self, password):#we added this method for Users table only , to use it on ((authentication)) later on
        if password == self.Password:return True
        else:return False


#Define your other entites (tables) below
