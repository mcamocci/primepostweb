import pymysql
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from model import PosterInfo,Database


class PosterInfoDao:

    def __init__(self):
        cursorConnection=Database.Database.getCursorConnection()
        self.cursor=cursorConnection['cursor']
        self.connection=cursorConnection['connection']

    def getAllPosterInfo(self):
        rows=self.cursor.execute("SELECT uploader.id as poster_id,uploader.name as poster_name,count(post.poster_id) as posts FROM uploader LEFT JOIN post ON uploader.id=post.poster_id GROUP BY uploader.id;")
        self.connection.close()
        return self.cursor.fetchall()


    def getAllPosterPost(self):
        pass

    def deletePosterPost(self,id):
        pass


def main():
    postdao=PosterInfoDao()
    print(postdao.getAllPosterInfo())


if __name__=="__main__":main()
