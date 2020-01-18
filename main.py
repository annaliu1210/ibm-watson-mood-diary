import os
import ast
import json
import pyrebase
from flask import Flask, render_template, redirect, url_for, request
from dotenv import load_dotenv
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from config import Config
from forms import DiaryEntry


app = Flask(__name__)
app.config.from_object(Config)
load_dotenv()

config = {
    "apiKey": os.getenv('apiKey'),
    "authDomain": os.getenv('authDomain'),
    "databaseURL": os.getenv('databaseURL'),
    "projectId": os.getenv('projectId'),
    "storageBucket": os.getenv('storageBucket'),
    "messagingSenderId": os.getenv('messagingSenderId'),
    "appId": os.getenv('appId'),
    "measurementId": os.getenv('measurementId')
}

firebase = pyrebase.initialize_app(config)


def tone_analyzer_api(text):
    authenticator = IAMAuthenticator(os.getenv('IBM_API_KEY'))
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )
    tone_analyzer.set_service_url(os.getenv('IBM_URL'))
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    result = json.dumps(tone_analysis, indent=2)
    return result


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Return the home page to submit a text entry for mood analysis.
    """
    form = DiaryEntry()
    if form.validate_on_submit():
        diary = form.text.data
        mood_json = json.loads(tone_analyzer_api(diary))['sentences_tone']
        mood_dict = [{'entry': diary, 'result': mood_json}]
        return render_template('results.html', entries=mood_dict)
    return render_template('index.html', form=form)


@app.route('/results', methods=['GET', 'POST'])
def results():
    """
    Return the results page with entries and their mood analysis from the database.
    """
    db = firebase.database()
    entries = db.child("entries").get()
    mood_results = [{'entry': entry['entry'], 'result': ast.literal_eval(entry['result'])}
                    for entry in entries.val()[1:]]
    return render_template('results.html', entries=mood_results)


if __name__ == "__main__":
    app.run('localhost', 5000, debug=True)
