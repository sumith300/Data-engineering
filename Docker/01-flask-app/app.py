from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'This is the about page!'

@app.route('/contact')
def contact():
    return 'This is the contact page!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True )