from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/")
def home():
    name = "static/images/{}.png".format(str(randint(4,29)))
    name1 = "static/images/{}.png".format(str(randint(4, 29)))
    name2 = "static/images/{}.png".format(str(randint(4, 29)))
    print(name,name1,name2)
    return render_template("index.html",name = name,name1 = name1,name2 = name2)

if __name__ == "__main__":
    app.run(debug=True,port=5252)