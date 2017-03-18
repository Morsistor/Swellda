from flask import Flask, url_for, render_template, request
app = Flask(__name__)

# The Legend of Swellda

@app.route("/")
def start():
    return render_template("start.html")

@app.route("/<location>")
def loc(location):
    inv = request.args.getlist('inv')
    
    inv_as_query = ""
    for item in inv:
        inv_as_query = inv_as_query + "inv=" + item + "&"

    return render_template(location + ".html", inv=inv, inv_as_query=inv_as_query)

# Inventory
# sword, shield, leather equipment, glass of milk, protein shake, barbell, sunglasses, Zelda's innocence, peanutbutter, steroids


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