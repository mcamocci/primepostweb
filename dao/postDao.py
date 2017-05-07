import pymysql
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from model import Database


class PostDao:
    def __init__(self):
        pass

    def getAllPost(self,id=0):
        cursor=Database.Database.getCursor()
        querry="SELECT post.id as post_id,post.content as content,post.date as date FROM post WHERE post.poster_id={};".format(id)
        rows=cursor.execute(querry)
        return cursor.fetchall()

    def deletePost(self,post_id):
        pass

    def updatePost(self,post_id,**kwargs):
        pass
