import pymysql
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from model import Database

class LoginDao:

    @staticmethod
    def login(user,ident):
        cursorConnection=Database.Database.getCursorConnection()
        cursor=cursorConnection['cursor']
        connection=cursorConnection['connection']

        identification=connection.escape(ident)
        username=connection.escape(user)
        querry="SELECT * FROM AdminUser WHERE identification={} AND username={}".format(identification,username)
        rows=cursor.execute(querry)
        if rows>0:
            connection.close()
            cursor.close()
            return True
        cursor.close()
        connection.close()
        return False
