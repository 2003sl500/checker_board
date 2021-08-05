from flask import Flask, app, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/single/<int:x>')
def single(x):
    return render_template("index.html", x = x, y = 0)

@app.route('/double/<int:x>/<int:y>')
def double(x,y):
    return render_template("index.html", x = x, y = y)

@app.route('/four/<int:x>/<int:y>/<string:color1>/<string:color2>')
def four(x,y,color1,color2):
    return render_template("index.html", x = x, y = y, color1 = color1, color2 = color2)

if __name__ == "__main__":
    app.run(debug=True)
