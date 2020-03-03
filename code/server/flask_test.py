#coding=utf-8
from flask  import Flask
import json
from flask import request
imooc_url = "https://www.imooc.com/passport/user/login?username=15800816652&password=tangjing1995"
app = Flask(__name__)

@app.route("/")
def login():
    data =json.dumps({

        "username" : "123456",
        "password" : "qweqe"
    })
    return data


@app.route("/passport/user/login",methods=["GET"])
def Home():
    username = request.args.get("username")
    password = request.args.get("password")
    if username and password :
        data =json.dumps({

           "username" : username,
            "password" : password
        })
    else:

        data="你输入的参数有误"
    return data

@app.route("/passport/user/post_login",methods=["POST"])
def post_login():
    request_method = request.method
    if request_method =="POST":
        username = request.args.get("username")
        password = request.args.get("password")
        data = json.dumps({
            "username": username,
            "password": password,
            "message" : "登录成功",
            "code"    : 200,
            })
    else:
        data = json.dumps({
                "message" : "你输入的参数有误",
        })
    return data

if __name__ == '__main__':
    app.run()

    pass