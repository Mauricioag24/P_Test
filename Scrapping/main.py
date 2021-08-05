from flask import Flask, jsonify
## local
from models.models import extract_products, to_json
app = Flask(__name__)
products =[]
products.extend(extract_products())
dic = to_json(products)

@app.route('/')
def hi():
    return jsonify(dic)
if __name__ == '__main__':
    app.run(host='localhost', debug=False)