from flask import Flask, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/hello")
def hello():
    param1 = request.args.getlist('inventory')
    print(param1)
    print(request.args)
    return "Inventory: {}".format(param1)

@app.route("/hyrulemarketplace")
def hyrulemarket():
    return render_template("hyrulemarketplace.html")

@app.route("/templ/")
@app.route("/templ/<var>")
def template(var=None):
    return render_template("templ.html", var=var)

@app.route("/post/<int:num>/")
def usernum(num):
    return "This is post #{numb}".format (numb=num) + ". LOL random!"

if __name__ == "__main__":
    app.run()