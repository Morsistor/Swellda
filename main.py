from flask import Flask, url_for, render_template, request
app = Flask(__name__)


@app.route("/hyrulemarketplace")
def hyrulemarket():
    return render_template("hyrulemarketplace.html")

@app.route("/castleyard")
def yard():
    return render_template("castleyard.html")

@app.route("/castledun")
def dun():
    return render_template("castledun.html")

@app.route("/castlebed")
def bed():
    return render_template("castlebed.html")

# @app.route("/hello/")
# def hello():
#     param1 = request.args.getlist('inventory')
#     print(param1)
#     print(request.args)
#     return "Inventory: {}".format(param1)

# @app.route("/user/<name>/")
# def helloname(name):
#     return "Hello " + name + ' !'

# @app.route("/templ/")
# @app.route("/templ/<var>")
# def template(var=None):
#     return render_template("templ.html", var=var)

# @app.route("/post/<int:num>/")
# def usernum(num):
#     return "This is post #{numb}".format (numb=num) + ". LOL random!"

if __name__ == "__main__":
    app.run()