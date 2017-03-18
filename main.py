from flask import Flask, url_for, render_template, request, redirect
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

    if location == 'hyrulegym' and 'barbell' not in inv:
        return redirect(url_for('loc', location='nobarbell'))
    
    return render_template(location + ".html", inv=inv, inv_as_query=inv_as_query)

if __name__ == "__main__":
    app.run()