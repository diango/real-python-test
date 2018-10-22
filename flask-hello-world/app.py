# ----- Flask Hello World ----- #

# import the flask class from flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# debugging mode
app.config["DEBUG"] = True

# use the decorator pattern to
# link the view function to a url
# static route
@app.route("/")
@app.route("/hello")


# define the view using function, wich returns a string
def hello_world():
    return "Hello, World?!?!?!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

# Dynamic route with explicit code status
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return f"Hello, {name}", 200
    else:
        return "Not Found", 404


# start the development server unsing the run() method
if __name__ == "__main__":
    app.run()
