from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/api/the_eye")
def the_eye():
    return "The_Eye"    

if __name__ == '__main__':
    # run app in debug mode on port 5000 - http://127.0.0.1:5000
    app.run(debug=True, port=5000)    