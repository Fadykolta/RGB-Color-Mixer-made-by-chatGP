from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        r = int(request.form["red"])
        g = int(request.form["green"])
        b = int(request.form["blue"])
        mixed_color = (r, g, b)
        return render_template("index.html", mixed_color=mixed_color)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
