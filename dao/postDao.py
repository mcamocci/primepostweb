import pymysql
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from model import Database
from werkzeug import secure_filename


class PostDao:

    def __init__(self):
        self.cursorConnection=Database.Database.getCursorConnection()
        self.cursor=self.cursorConnection['cursor']
        self.connection=self.cursorConnection['connection']

    def getAllPost(self,id=0):
        querry="SELECT post.id as post_id,post.content as content,post.date as date FROM post WHERE post.poster_id={};".format(id)
        rows=cursor.execute(querry)
        return cursor.fetchall()

    def deletePost(self,post_id):
        connection=cursorConnection['connection']
        resourceCounts="SELECT * FROM resource where resource.post_id={}".format(post_id)
        rescount=cursor.execute(resourceCounts)

        if rescount>0:
            querryResource="DELETE FROM resource WHERE resource.post_id = {}".format(post_id)
            rows=cursor.execute(querryResource)
            if rows>0:
                querry="DELETE FROM post WHERE post.id = {}".format(post_id)
                rows=cursor.execute(querry)
                connection.commit()
                return rows
        else:
            querry="DELETE FROM post WHERE post.id = {}".format(post_id)
            rows=cursor.execute(querry)
            connection.commit()
            return rows

    def updatePost(self,post_id,**kwargs):
        pass

    def insertPost(self,user_id,postDescription):
        querry="INSERT INTO post(content, poster_id) VALUES (%s, %s)"
        rows=self.cursor.execute(querry,(postDescription,int(user_id)))
        last_id=self.connection.insert_id()
        self.connection.commit()
        return last_id

    def insertPostResource(self,post_id,file_url):
        querry="INSERT INTO resource(url, post_id) VALUES (%s , %s )"
        self.cursor.execute(querry,(file_url,post_id))
        self.connection.commit()
