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
        querry="SELECT post.id as post_id,post.content as content,post.date as date FROM post WHERE post.poster_id={} ORDER BY post.id DESC;".format(id)
        rows=self.cursor.execute(querry)
        self.connection.close()
        return self.cursor.fetchall()

    def deletePost(self,post_id):
        connection=self.cursorConnection['connection']
        resourceCounts="SELECT * FROM resource where resource.post_id={}".format(post_id)
        rescount=self.cursor.execute(resourceCounts)

        if rescount>0:
            querryResource="DELETE FROM resource WHERE resource.post_id = {}".format(post_id)
            rows=self.cursor.execute(querryResource)
            if rows>0:
                querry="DELETE FROM post WHERE post.id = {}".format(post_id)
                rows=self.cursor.execute(querry)
                self.connection.commit()
                self.connection.close()
                return rows
        else:
            querry="DELETE FROM post WHERE post.id = {}".format(post_id)
            rows=self.cursor.execute(querry)
            self.connection.commit()
            self.connection.close()
            return rows

    def updatePost(self,post_id,**kwargs):
        pass

    def insertPost(self,user_id,postDescription):
        querry="INSERT INTO post(content, poster_id) VALUES (%s, %s)"
        rows=self.cursor.execute(querry,(postDescription,int(user_id)))
        last_id=self.connection.insert_id()
        self.connection.commit()
        self.connection.close()
        return last_id

    def insertPostResource(self,post_id,file_url):
        querry="INSERT INTO resource(url,type, post_id) VALUES (%s , %s ,%s)"
        file_extension=file_url.split('.')[1]
        self.cursor.execute(querry,("http://192.168.43.234/superbell_backend/mediaUploads/"+file_url,file_extension,post_id))
        self.connection.commit()
        self.connection.close()
