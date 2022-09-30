from flask import Flask, render_template, request
from simple_tracker import get_product
from tinydb import TinyDB, Query



app = Flask("Amazon Price Tracker")

# route for the home page
@app.route("/" , methods=["GET"])
def index():
    return render_template("index.html")

# route to search 
@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name')
    user_db = TinyDB('json/'+name+'.json')
    products = user_db.all()
    if name == 'product':
        result = {'products':[]}
        for i in products:
            result['products'].append(i)
    else:
        result = {'email':[]}
        for i in products:
            result['email'].append(i)
    return result

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()

    if data['type'] == 'url':
        user_product = TinyDB("json/product.json")
        while True:
            status = True
            try:
                product = get_product(data['data'])
            except Exception:
                status = False
                pass
            if status:
                break
        product_search = Query()
        find_product = user_product.search(product_search.id == product['id'])
        if find_product == []:
            user_product.insert(product)
            return "Tracking "+product['product_title']
        else:
            return product['product_title']+" is already in your tracking list."
    elif data['type'] == 'email':
        user_email = TinyDB("json/email.json")
        email_search = Query()
        find_email = user_email.search(email_search.email == data['data'])
        if find_email == []:
            user_email.insert({"email":data['data']})
            return "Email Saved."
        else:
            return "Email already exist."


@app.route('/remove', methods=['POST'])
def remove():
    data = request.get_json()
    if data['type'] == 'product':
        user_product = TinyDB("json/product.json")
        product_search = Query()
        user_product.remove(product_search.id == data['data'])
        return "Product Deleted."
    elif data['type'] == 'email':
        user_product = TinyDB("json/email.json")
        product_search = Query()
        user_product.remove(product_search.email == data['data'])
        return "Email Deleted."

app.run(host='0.0.0.0',debug=False, port=10086)