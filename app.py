from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello_world():
    return 'Hello World!'

@app.route('/addo')
def addo():
    return 'Hello, Addo'

if __name__ == "__main__":
    app.run(debug=True)