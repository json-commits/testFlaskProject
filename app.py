from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def landing():  # put application's code here
    return redirect("https://www.google.com/", code=302)


if __name__ == '__main__':
    app.run()

