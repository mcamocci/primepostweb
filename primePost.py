from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import render_template
from flask import url_for
from dao import posterInfoDao,postDao

app=Flask(__name__)

#you will be redirect if not logged in else you directed to poster aka home
@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for('home'))
    return render_template("index.html")


#this is for the poster info pannel after the login
@app.route("/home")
def home():
    if "user_id" in session:
        posters=posterInfoDao.PosterInfoDao().getAllPosterInfo()
        context={'posterInfos':posters}
        return render_template("poster.html",**context)
    else:
        return render_template("index.html")


#the things typed on form handled here
@app.route("/login",methods=["POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username",None)
        if  username != None:
            session["user_id"]=username
            return redirect(url_for('home'))
        else:
            return "please fill the form {}".format(str(request.form.get("username","emmanuel")))
    else:
        return "you are faking request"

#the logout handler function
@app.route("/logout")
def logout():
    if "user_id" in session:
        session.pop("user_id",None)
        return render_template("index.html")
    else:
        return render_template("index.html")

#much is not done yet maybe removed later
@app.route("/admins")
def admin():
    return redirect(url_for('index'))

#getting posts from the specified channel
@app.route("/posts/<int:id>")
def posts(id=None):
    if id != None:
        posts=postDao.PostDao().getAllPost(id)
        context={'posts':posts}
        return render_template("home.html",**context)

    return redirect(url_for('index'))

@app.route("/deletePost/<int:id>")
def deletePost(id=0):
    return "you want to delete item {}".format(id)

if __name__=="__main__":
    app.secret_key="haikarose"
    app.run(debug=True)
