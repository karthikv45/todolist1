from flask import flask,render_template
app = flask(_name_)
@app.route("/")
@app.route("/home")

def home():
    return render_template(index.html)
if _name_=="_main_":
    app.run(debug=True)