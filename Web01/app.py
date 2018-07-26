
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
        "title": "Thơ con cóc",
        "content": "àdsf àdsgf àgdsg",
        "author": "aenfdf",
        "gender": 0
    },
        {
        "title": "Thơ con cóc",
        "content": "àdsf àdsgf àgdsg",
        "author": "aenfdf",
        "gender": 1
    },
        {
        "title": "Thơ con cóc",
        "content": "àdsf àdsgf àgdsg",
        "author": "aenfdf",
        "gender": 0
    }
    ]


    return render_template(
        "index.html", 
        posts=posts
        )


@app.route("/hello")

def hello():
    return "Hello C4E 19"


@app.route("/say-hi/<name>/<age>")
def sayhi(name, age):
    return "Hi {0}. You are {1} years old".format(name, age)

if __name__ == '__main__':
  app.run(debug=True)
