from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import render_template
from flask import url_for

app=Flask(__name__)

@app.route("/")
def index():
    if "user_id" in session:
        return render_template("poster.html")
    return render_template("index.html")

@app.route("/home")
def home():
    if "user_id" in session:
        context={'age':22,'name':"Graciana"}
        return render_template("poster.html",**context)
    else:
        return render_template("index.html")

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

@app.route("/logout")
def logout():
    if "user_id" in session:
        session.pop("user_id",None)
        return render_template("index.html")
    else:
        return render_template("index.html")

@app.route("/admins")
def admin():
    return redirect(url_for('index'))

@app.route("/posts/<int:id>")
def posts(id=None):
    if id != None:
        return render_template("home.html")
    pass

if __name__=="__main__":
    app.secret_key="haikarose"
    app.run(debug=True)
