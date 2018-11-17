from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!"
@app.route("/login")
def login():
    return "login page"
@app.route("/menu")
def menu():
    return "menu page"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
