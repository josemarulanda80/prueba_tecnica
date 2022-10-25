from flask import Flask

app=Flask(__name__)


@app.route("/")
def index():
    return "Hola"

if __name__=="main":
    app.run(debug=True)