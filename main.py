from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "This is home from api."

@app.route("/getdetails/<username>")
def get_user(username):
    return "Hi " + username + " . We are getting this from our api."

if __name__ == "__main__":
    app.run(debug=True)