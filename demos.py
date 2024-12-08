from flask import Flask
app=Flask(__name__)
@app.route("/hello/<string:track>")
def hello(track):
    return f"hello people!Welcome to HC {track} Bootcamp1 session"
@app.route("/")
def welcome():
    return "welcome to the hc"
@app.route("/something")
def something():
    return "welcome to the hc"
if __name__ == "__main__":
    app.run(debug=True)
    
