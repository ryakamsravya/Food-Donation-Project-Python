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
    return "this is new route"
@app.route("/hc/string:anything>")
def hc(anything):
    if anything=="CAD":
        return redirect(url_for('hello',track=anything))
    else:
        return redirect(url_for('something'))

if __name__ == "__main__":
    app.run(debug=True)
    
