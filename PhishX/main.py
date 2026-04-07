from flask import Flask, render_template, request
from analyser import analyze_email_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        email_text = request.form.get("email")
        result = analyze_email_text(email_text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=5000)
