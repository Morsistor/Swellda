from flask import Flask, url_for, render_template, request, redirect
import random
app = Flask(__name__)


# The Legend of Swellda


# start page
@app.route("/")
def start():
    return render_template("start.html")


# ingame pages
@app.route("/<location>")
def loc(location):
    inv = request.args.getlist('inv')
    name = request.args.getlist('name')
    gender = request.args.getlist('gender')
    ads = request.args.getlist('ads')


    inv_as_query = ""
    for item in inv:
        inv_as_query = inv_as_query + "inv=" + item + "&"
    
    inv_as_query_minus_mask = ""
    for item in inv:
        if item != "Leather Mask":
            inv_as_query_minus_mask = inv_as_query_minus_mask + "inv=" + item + "&"
    
    adnum = 3
    adnum = random.sample(range(4), 1)
    adnums = ""
    adnums = str(adnum)
    # if ads == "yes":

    if location == 'hyrulegym' and 'Protein Shake' not in inv:
        return redirect(url_for('loc', location='noproteinshake', inv=inv))

    if location == 'shop' and 'Leather Mask' not in inv:
        return redirect(url_for('loc', location='shop2', inv=inv))

    return render_template(location + ".html", inv=inv, inv_as_query=inv_as_query, inv_as_query_minus_mask=inv_as_query_minus_mask, adnums=adnums)

if __name__ == "__main__":
    app.run()