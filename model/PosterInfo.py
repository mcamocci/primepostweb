
class PosterInfo:

      def __init__(self,**kwargs):
          self.__name=kwargs.get("name","nil")
          self.__id=kwargs.get("id",0)
          self.__postCount=kwargs.get("postCount",0)

      def getName(self):
          return self.__name
      def getId(self):
          return self.__id
      def getPostCount(self):
          return self.__postCount

      def __str__(self):
          return "This is PosterInfo Class for accessing , uploader ,uploader id and uploader post count"

      def __repr__(self):
          return "This is PosterInfo Class for accessing , uploader ,uploader id and uploader post count"
