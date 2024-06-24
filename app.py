from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route('/screener')
def screener():
    return render_template('screener.html')

if __name__ == '__main__':
    app.run(debug=True)
