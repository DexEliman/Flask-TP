"""
Exo 1

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Hello World! ')

if __name__ == '__main__':
    app.run()

=============================
Exo 2    

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

if __name__ == '__main__':
    app.run()

=========================
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

@app.route("/ciel")
def ciel():
    return render_template("ciel.html")

@app.route("/snir")
def snir():
    return render_template("snir.html")

@app.route("/etudes-sup")
def etudes_sup():
    return render_template("etudes-sup.html")

if __name__ == "__main__":
    app.run(debug=True)