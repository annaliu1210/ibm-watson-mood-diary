from flask import Flask, render_template
from config import Config
from forms import DiaryEntry

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Return the home page.
    """
    form = DiaryEntry()
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run('localhost', 5000, debug=True)
