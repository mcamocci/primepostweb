#!usr/bin/python3
import pymysql

class Database:

    database=pymysql.connect("localhost","root","haikarose","mediaroseDb")

    def __init__(self,host="",username="",password="",database=""):
        pass

    @staticmethod
    def getCursor(**kwargs):
        host=kwargs.get("host","localhost")
        username=kwargs.get("username","root")
        database_name=kwargs.get("database","mediaroseDb")
        password=kwargs.get("password","haikarose")

        database=pymysql.connect(host,username,password,database_name)
        return database.cursor(pymysql.cursors.DictCursor)

    def closeConnection(self):
        pass


def main():
    pass
if __name__=="__main__":main()
