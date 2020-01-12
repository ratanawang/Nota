from flask import Flask, request, render_template, send_from_directory, flash, redirect
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
# from firebase_admin import storage

# Initialize app with environment variable
default_app = firebase_admin.initialize_app()

user_logged_in = False

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

    # Test user authentication stuff
    # input register
# email = input("(create acc) enter email: ")
# password = input("(create acc) enter password: ")
# sample_data = input("enter some sample data: ")

    # create user and add data to Firestore
# try:
#     user = auth.create_user(email=email, password=password, disabled=False)
# except Exception:
#     print(u'Account already exists')
# print(user.uid)
# data = {
#     u'uid': user.uid,
#     u'password': password,
#     u'note count': 0
# }
# db.collection(u'users').document(user.uid).set(data)

# data = {
#     u'sample_data': sample_data
# }
# db.collection(u'users').document(user.uid).collection(u'sample_data').document(u'set').set(data)

    # clear variables
# email = ""
# password = ""
# sample_data = ""

    # input sign in
# input_email = input("(sign in) enter email: ")
# input_password = input("(sign in) enter password: ")

    # check user, password and print sample text
# try:
#     user = auth.get_user_by_email(input_email)
# except Exception:
#     print("error with inputted email")

    # get document, convert to dict and get password
# doc_ref = db.collection(u'users').document(user.uid).get()
# doc = doc_ref.to_dict()
# get_password = doc["password"]
#
# if input_password == get_password:
#     print(user.uid)
#     doc_ref = db.collection(u'users').document(user.uid)
#     try:
#         doc = doc_ref.get()
#         print(u'Document data: {}'.format(doc.to_dict()))
#     except Exception:
#         print(u'No document found')
# else:
#     print('wrong password')

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route('/css/<path>')
def send_style(path):
    return send_from_directory('css', path)


@app.route('/fonts/<path>')
def send_fonts(path):
    return send_from_directory('fonts', path)


@app.route('/img/<path>')
def send_img(path):
    return send_from_directory('img', path)


@app.route('/js/<path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/scss/<path>')
def send_scss(path):
    return send_from_directory('scss', path)


@app.route('/login', methods=['POST', 'GET'])
def submit():
    global user_logged_in
    if request.form['action'] == 'Sign In':
        # get email and password from login/register form
        input_email = request.form['email']
        input_password = request.form['password']

        # check user and password
        try:
            user = auth.get_user_by_email(input_email)
        except firebase_admin.exceptions.NotFoundError:
            print("Account not found, sign up instead!")
        except Exception:
            print("General error")
            return render_template('login.html')
        else:
            # get document, convert to dict and get password
            doc_ref = db.collection(u'users').document(user.uid).get()
            doc = doc_ref.to_dict()
            get_password = doc["password"]

            if input_password == get_password:
                print('Signed in')
                user_logged_in = True
                return redirect('index2.html')
            else:
                print('wrong password')
                return render_template('login.html')

    elif request.form['action'] == 'Sign Up':
        # get email and password from login/register form
        input_email = request.form['email']
        input_password = request.form['password']

        # check user and password
        try:
            user = auth.get_user_by_email(input_email)
        except firebase_admin.exceptions.NotFoundError:
            # setup account stuff
            try:
                user = auth.create_user(email=input_email, password=input_password, disabled=False)
            except Exception:
                print('General error')
                return render_template('login.html')
            else:
                print('Account created successfully')
                # get document, convert to dict and get password
                data = {
                    u'uid': user.uid,
                    u'password': input_password,
                    u'note count': 0
                }
                db.collection(u'users').document(user.uid).set(data)
                user_logged_in = True
                return redirect('/')
        except Exception:
            print("General error")
            return render_template('login.html')
        else:
            # get document, convert to dict and get password
            doc_ref = db.collection(u'users').document(user.uid).get()
            doc = doc_ref.to_dict()
            get_password = doc["password"]

            if input_password == get_password:
                user_logged_in = True
                return redirect('index2.html')
            else:
                print('wrong password')
                return render_template('login.html')
    else:
        print('ERROR')


if __name__ == "main":
    app.run(debug=True)
