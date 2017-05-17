#!usr/bin/python3
from flask import url_for
from flask import redirect

def haikarose_login_required(sessionObject=None,urlIndex=None,urlHome=None):
    def decorated(fun):
        def wrapper():
            if "user_id" in sessionObject:
                return redirect(url_for(urlHome))
            else:
                return redirect(url_for(urlIndex))
        return wrapper
    return decorated
