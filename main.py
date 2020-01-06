from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Return the home page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run('localhost', 5000, debug=True)
