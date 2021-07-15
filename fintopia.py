from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '<div style="font-size: 100px; margin-top: 200px;"><center>Under Construction</center></div>'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
