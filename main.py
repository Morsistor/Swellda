from flask import Flask, url_for, render_template, request
app = Flask(__name__)

# The Legend of Swellda

@app.route("/")
def start():
    return render_template("start.html")

@app.route("/hyrulemarket")
def hyrulemarket():
    return render_template("hyrulemarket.html")

@app.route("/castleyard")
def yard():
    return render_template("castleyard.html")

@app.route("/castledun")
def dun():
    return render_template("castledun.html")

@app.route("/castlebed")
def bed():
    return render_template("castlebed.html")

@app.route("/hyrulegym")
def gym():
    return render_template("hyrulegym.html")

@app.route("/workout")
def work():
    return render_template("workout.html")

@app.route("/basar")
def basar():
    return render_template("hyrulebasar.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

# Inventory
# sword, shield, leather equipment, glass of milk, protein shake, barbell, sunglasses, Zelda's innocence, peanutbutter, steroids

@app.route("/i/<location>/")
def inventory(location=None):
    param1 = request.args.getList('inv')
    return "Inventory: {}".format(param1)

# @app.route("/hello/")
# def hello():
#     param1 = request.args.getlist('inv')
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