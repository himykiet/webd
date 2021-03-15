from flask import Flask,render_template,request

app = Flask("app")

@app.route("/")
def home():
      print("i'm in home page")
      page=render_template("home.html")
      return (page)

@app.route("/login")
def login():
      page=render_template("login.html")
      return(page)
@app.route("/userpage", methods=["GET"])
def userpage():
      u=request.args.get("user")
      p=request.args.get("pass")
      page=render_template("user.html",username=u)
      return (page)