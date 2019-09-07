from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/action_page.php")
def action_page():
    return render_template("action_page.php.html")

if __name__ == "__main__":
    app.run(debug=True)