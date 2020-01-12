from flask import Flask, request, render_template, send_from_directory
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize app with environment variable
default_app = firebase_admin.initialize_app()

# Setup services
db = firestore.client()

# Test adding data to database
# doc_ref = db.collection(u'users').document(u'wchow').collection(u'testing').document(u'notes' + num)
# doc_ref.set({
#     u'first': u'Wes',
#     u'last': u'Chow',
#     u'born': 2003
# })

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "main":
    app.run(debug=True)
