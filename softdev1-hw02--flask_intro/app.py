from flask import Flask

app = Flask(__name__) 

@app.route("/")
def index():
    return "I swear my future hws will be of higher quality cuz it's 4AM rn"

@app.route("/a")
def brown():
    return "I swear my future hws will be of higher quality cuz it's 4AM rn"

@app.route("/b")
def dw():
    return "I swear my future hws will be of higher quality cuz it's 4AM rn"

if __name__ == "__main__":
    app.run(debug=True)
