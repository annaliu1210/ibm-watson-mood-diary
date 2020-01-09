from flask import Flask, render_template, redirect, url_for, request
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
    if form.validate_on_submit():
        diary = form.text.data
        return redirect(url_for('results', diary=diary))
    return render_template('index.html', form=form)


@app.route('/results', methods=['GET', 'POST'])
def results():
    """
    Return the results.
    """
    return render_template('results.html', diary=request.args.get('diary'))


if __name__ == "__main__":
    app.run('localhost', 5000, debug=True)
