from flask import Flask,render_template, jsonify,request
from flask import redirect,url_for
from flask.wrappers import Request

app = Flask(__name__)


#return hello
@app.route('/')
def home():
    return 'Hello!'

#return Json
@app.route('/api/get-json')
def hello():
    return jsonify(hello='world')


@app.route("/<name>,<age>")
def user(name ,age):
    print(request.args)
    yob=2021

    return f"hello {name}! you are {age}. You born in {yob}"
#Post method
@app.route('/login', methods = [ "POST" , "GET"])
def login():
    if request.method == "POST" :
        na=request.form.get("nm")
        age=request.form.get("ag")
        yob=2020-int(age)
        return render_template('age_finder.html', n = na , a = age, yob = yob)
    else:
        return render_template('login.html')

if __name__ == '__main__':
 app.run()