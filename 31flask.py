from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"
@app.route('/newpage')
def newpage():
    return "Now You Are In New Page"
@app.route('/introduction/<name>')
def intro(name):
    return "I am %s " %name 

if __name__ == '__main__':
    app.run()