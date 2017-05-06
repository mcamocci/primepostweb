import pymysql
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from model import PosterInfo,Database


class PosterInfoDao:

    def __init__(self):
        pass

    def getAllPosterInfo(self):
        cursor=Database.Database.getCursor()
        rows=cursor.execute("SELECT uploader.id as poster_id,uploader.name as poster_name,count(post.poster_id) as posts FROM uploader LEFT JOIN post ON uploader.id=post.poster_id GROUP BY uploader.id;")
        return cursor.fetchall()

    def getAllPosterPost(self):
        pass

    def deletePosterPost(self,id):
        pass


def main():
    postdao=PosterInfoDao()
    print(postdao.getAllPosterInfo())

if __name__=="__main__":main()
