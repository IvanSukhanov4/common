from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/<device>/info')
def get_info(device):
    info = [products for products in get_data()
            if device.replace('_', ' ').lower()
            in (v.lower() for v in products.values())][0]
    return render_template("info.html", info=info, device=device)


@app.route('/author')
def get_author():
    return render_template("author_info.html")


if __name__ == "__main__":
    app.run(debug=True)
