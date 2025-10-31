from flask import render_template, request
import dao
from saleapp import app
import math


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    page = request.args.get("page")
    prods = dao.load_products(q=q, cate_id=cate_id, page=page)
    pages = math.ceil(dao.count_product()/app.config["PAGE_SIZE"])
    return render_template("index.html", prods=prods, pages=pages)

@app.route("/products/<int:id>")
def details(id):

    return render_template("products-details.html", prod=dao.get_product_by_id(id))

@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }

@app.route("/login")
def login_my_user():
    return render_template("login.html")

if __name__== "__main__":
    with app.app_context():
        app.run(debug=True)