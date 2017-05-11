from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import render_template
from flask import url_for,flash
from dao import posterInfoDao,postDao
from werkzeug import secure_filename
import os

app=Flask(__name__)
app.config['UPLOAD_FOLDER']='/var/www/html/superbell_backend/mediaUploads'


########################################################################################
########################################################################################
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

########################################################################################
########################################################################################
#you will be redirect if not logged in else you directed to poster aka home
@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for('home'))
    return render_template("index.html")

########################################################################################
########################################################################################
#this is for the poster info pannel after the login
@app.route("/home")
def home():
    if "user_id" in session:
        posters=posterInfoDao.PosterInfoDao().getAllPosterInfo()
        context={'posterInfos':posters}
        return render_template("poster.html",**context)
    else:
        return render_template("index.html")

########################################################################################
########################################################################################
#the things typed on form handled here
@app.route("/login",methods=["POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username",None)
        if  username != None:
            session["user_id"]=1
            return redirect(url_for('home'))
        else:
            return "please fill the form {}".format(str(request.form.get("username","emmanuel")))
    else:
        return "you are faking request"

########################################################################################
########################################################################################
#the logout handler function
@app.route("/logout")
def logout():
    if "user_id" in session:
        session.pop("user_id",None)
        return render_template("index.html")
    else:
        return render_template("index.html")

########################################################################################
########################################################################################
#much is not done yet maybe removed later
@app.route("/admins")
def admin():
    return redirect(url_for('index'))

########################################################################################
########################################################################################
#getting posts from the specified channel
@app.route("/posts/<int:id>")
def posts(id=None):
    if id != None:
        session['current_poster']=id
        posts=postDao.PostDao().getAllPost(id)
        context={'posts':posts}
        return render_template("home.html",**context)

    return redirect(url_for('index'))

########################################################################################
########################################################################################

#getting posts from the specified channel
@app.route("/publish")
def publish():
    return render_template("publishPost.html")

########################################################################################
########################################################################################
@app.route("/publish",methods=["POST"])
def publishPost():
    if request.method=="POST":
        fileList=request.files.getlist("RESOURCES[]")
        postDescription=request.form.get("CONTENT",None)
        uploaded_file_path=list()

        for file in fileList:
            if file:
                filename=secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
                uploaded_file_path.append(filename)

        user_id=session["user_id"]
        poster_id=session['current_poster']

        inserted_post_id=postDao.PostDao().insertPost(user_id,postDescription)

        if(len(uploaded_file_path)>0):
            for fileurl in uploaded_file_path:
                postDao.PostDao().insertPostResource(inserted_post_id,fileurl)
        return redirect(url_for('posts',id=poster_id))

    else:
        return redirect(url_for('posts',id=poster_id))

########################################################################################
########################################################################################
@app.route("/deletePost/<int:id>")
def deletePost(id=0):
    row_affected=postDao.PostDao().deletePost(id)
    flash("The delete operation has completed successfully , Click to dismiss")
    if "current_poster" in session:
        return redirect(url_for('posts',id=session['current_poster']))
    return redirect(url_for('index'))


if __name__=="__main__":
    app.secret_key="haikarose"
    app.run(debug=True)
