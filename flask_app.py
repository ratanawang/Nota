from flask import Flask, request, render_template, send_from_directory
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from firebase_admin import storage

# Initialize app with environment variable
default_app = firebase_admin.initialize_app()

# Setup services
db = firestore.client()
auth = firebase_admin.auth

# Test adding data to database
# doc_ref = db.collection(u'users').document(u'wchow')
# doc_ref.set({
#     u'first': u'Wes',
#     u'last': u'Chow',
#     u'born': 2003
# })

# Test creating user
# email = input("(create acc) enter email: ")
# password = input("(create acc) enter password: ")
# sample_data = input("enter some sample data: ")
#
# user = auth.create_user(email=email, password=password, disabled=False)
# email = ""
# password = ""
# sample_data = ""
#
# input_email = input("(sign in) enter email: ")
# input_password = input("(sign in) enter password: ")

# user = auth.get_user_by_email(input_email)

# print(user.passwordHash())
# if user.passwordHash == input_password:
#     print("got the user")

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "main":
    app.run(debug=True)
