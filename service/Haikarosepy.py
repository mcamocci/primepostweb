#!usr/bin/python3

def haikarose_login_required(session):
    def decfunc(fun):
        def wrapper():
            if "user_id" in session:
                func():
            else:
                return render_template("index.html")
        return wrapper()
