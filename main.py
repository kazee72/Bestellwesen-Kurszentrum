from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello/",methods=["POST","GET"])
@app.route("/hello/<name>",methods=["POST","GET"])
def hello(name=None):
    if request.method == "POST":
        print("request",request)
        #data in url fname = request.args.get("name")
        fname = request.form["name"]
        print("fname:",fname)

    return render_template("person.html",person=name)

@app.route("/upload",methods=["GET","POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["testfile"]
        print("files:",file)
        file.save("./test_upload2.txt")
    return render_template("upload.html")
                    


