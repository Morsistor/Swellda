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

if __name__ == "__main__":
    app.run()