from flask import Flask, render_template #render template is used for rendering html pages

app = Flask(__name__)  #creating a new web application

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)