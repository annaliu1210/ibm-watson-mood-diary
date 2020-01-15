# IBM Watson Mood Diary
IBM Watson Mood diary is a web application built under a backend Flask framework and frontend Bootstrap framework using a Firebase database.

The purpose of this application is to allow users to submit diary entries about their days to keep track of how they feel. With the use of IBM Watson's Tone Analyzer API, these diary entries are broken down by sentence and analyzed into different emotions.

## Setup Instructions
Clone the git repository:

    git clone https://github.com/BrandonTang/ibm-watson-mood-diary.git

Create a virtual environment and install the requirements:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Create a Tone Analyzer service by visiting the IBM Cloud Category:

    https://cloud.ibm.com/catalog/services/tone-analyzer
    
Create a Firebase database and connect it to your web application to obtain the configurations needed to connect:

    https://firebase.google.com/

Create a .env file with the below environment variables in the root directory found in the Manage section of your Tone Analyzer dashboard:

    IBM_API_KEY=IBM_API_KEY
    IBM_URL=IBM_URL
    apiKey=apiKey
    authDomain=authDomain
    databaseURL=databaseURL
    projectId=projectId
    storageBucket=storageBucket
    messagingSenderId=messagingSenderId
    appId=appId
    measurementId=measurementId
    
Locally run the application by entering the following in the command line:

    python main.py
