from flask import Flask
from views import views
from flask import Flask, flash, render_template, request, redirect, url_for, session
from flask import jsonify
from flask_dropzone import Dropzone
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from flask_cors import CORS
import random
import MySQLdb
import os
import time
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import config

import extractNotes

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)
app.register_blueprint(views, url_prefix="/")
app.config.update(
   UPLOADED_PATH = "/app/uploads",
   DROPZONE_MAX_FILE_SIZE = 1024,
   DROPZONE_TIMEOUT = 5*60*1000
)

dropzone = Dropzone(app)
CORS(app)
app.config['MYSQL_HOST'] = config.sql_host
app.config['MYSQL_USER'] = config.sql_user
app.config['MYSQL_PASSWORD'] = config.sql_password
app.config['MYSQL_DB'] = config.sql_user
os.environ['SENDGRID_API_KEY'] = config.api_key

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

mysql = MySQL(app)

Flag = False
filepath = os.path.join('RawNotes', 'RawNotes-tab.txt')
if os.path.exists('../RawNotes'):
    f = open(filepath, "r+")
    f.truncate()
def validatepw(password):
      a=0
      b=0
      c=0
      d=0
      if len(password)<8 or len(password)>20:
         return 0
      for i in password:
         if i.isupper():
            a+=1
         elif i.islower():
            b+=1
         elif i in '"!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"':
            c+=1
         elif i.isdigit():
            d+=1
      if a>=1 and b>=1 and c>=1 and d>=1 and a+b+c+d==len(password):
        return 1
      else:
         return 0


def validateUser(username):
    
    for i in username:
        if i in '"!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"':
            return 0
    if len(username)<8 or len(username)>20:
         return 0
    return 1

def validateEmail(email):
    a=0
    b=0
    for i in email:
        if i == '.':
            a += 1
        if i =='@':
            b += 1
    if a >=1 and b == 1:
        return 1
    else: 
        return 0
@app.route('/send-email', methods=['POST'])
def send_email():
    sender_email = request.get_json()['realEmail']
    reply_email = request.get_json()['email']
    sender_name = request.get_json()['name']
    message = request.get_json()['message']
    recipient_email = 'clabbusiness2023@gmail.com'

    # Create SendGrid message object
    message = Mail(
        from_email=(sender_email, sender_name),
        to_emails=recipient_email,
        subject='New message from your website! from {}'.format(reply_email),
        plain_text_content="{} said: ".format(reply_email) + message)

    try:
    # Initialize SendGrid client with API key
        sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

        # Send message via SendGrid API
        response = sg.send(message)

        # Return success message
        return 'Message sent successfully!'
    except Exception as e:
        # Return error message
        return 'An error occurred while sending the message: {}'.format(str(e))

@app.route('/loggedin')
def set_loggedin():
    loggedin = True
    return jsonify(variable=loggedin)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    global Flag
    filepath = os.path.join('RawNotes', 'RawNotes-tab.txt')
    if os.path.exists('RawNotes'):
        f = open(filepath, "r+")
        f.truncate()

    if request.method == 'POST':
        
        print("FLAg IS {} IN UPLOAD".format(Flag))
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        notes = extractNotes.midiConvert(f.filename)
        Tscript = extractNotes.run(notes)
        session["var"] = Tscript
        filepath = os.path.join('RawNotes', 'RawNotes-tab.txt')
        if not os.path.exists('RawNotes'):
            os.makedirs('RawNotes')
        f = open(filepath, "r")
        songnotes = f.read()
        
        
        
        songID = random.randrange(1000)
        print("DEBUG: SONG ID = "  + str(songID))
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO Tabs (Tablature, idSong) VALUES(%s,%s)''',(songnotes, songID))
        mysql.connection.commit()
        cursor.close()
        f.close()
    return {"tab" : songnotes}



@app.route('/display', methods = ['GET'])
def display():
    global Flag
    if request.method=='GET':
        time.sleep(0.5)
        with open('../RawNotes/RawNotes-tab.txt', 'r+') as f: 
            output = f.read()
            f.close()
        #filepath = os.path.join('RawNotes', 'RawNotes-tab.txt')
        #if os.path.exists('RawNotes'):
           # f = open(filepath, "r+")
            #f.truncate()    
        return {"tab" : output}
    

@app.route('/wipe', methods = ['GET'])
def wipe():
    filepath = os.path.join('../RawNotes', 'RawNotes-tab.txt')
    if os.path.exists('RawNotes'):
        f = open(filepath, "r+")
        f.truncate()
    return{"nullTab": ""}
     


@app.route('/retrieve')
def retrieve():
        if "var" in session:
            var = session["var"]
            return render_template('display.html', var = var)
        else:
            return render_template('display.html', var ='no data in session')

@app.route('/search', methods = ['POST', 'GET'])
def search(): 
        if request.method == 'GET':
            return render_template('search.html')

        if request.method == 'POST':
            songID = request.form['SongID']
            cursor = mysql.connection.cursor()
            cursor.execute('''SELECT * from Tabs WHERE idSong = (%s)''',(songID))
            data = cursor.fetchone()
            mysql.connection.commit()
            session["var"] = songID
            cursor.close()
            return render_template('display.html', var = songID)

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return ""
     
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        validPW = validatepw(password)
        if validPW == 0:
            flash("Please input a valid password. A valid password uses a number, a special character, a capital letter, and has a length between 8 and 20 characters.")
            return redirect(url_for('register'))
        validEmail = validateEmail(email)
        if validEmail == 0:
            flash("Please input a valid email address.")
            return redirect(url_for('register'))
        validUser = validateUser(username)
        if validUser == 0:
            flash("Please input a valid username. A valid username is at least 8 characters and contains no special characters.")
            return redirect(url_for('register'))
        idUser = random.randrange(100)
        cursor = mysql.connection.cursor()
        cursor.execute("select * from Users where (Username = '%s') OR (Email = '%s')" % (username, email))
        if cursor.rowcount == 0:
            if email and username and password:
                cursor.execute(''' INSERT INTO Users (Email,Username,Password,idUser) VALUES(%s,%s,%s,%s)''',(email,username,password,idUser))
                mysql.connection.commit()
                cursor.close()
                flash("User registered")
                return redirect(url_for('display'))
            else:
                flash("Please fill out all forms.")
                return redirect(url_for('register'))
        else:
            flash("Username or email already exists!")
            return redirect(url_for('register'))

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        loginusername = request.form['username']
        loginpassword = request.form['password']
        cursor = mysql.connection.cursor()
        ##sql ='SELECT idUser from Users WHERE Username = {0}'.format(loginusername)
        cursor.execute("select * from Users where (Username = '%s') AND (Password = '%s')" % (loginusername, loginpassword))
        if cursor.rowcount == 0:
            flash("User does not exist, try again, or go sign up!")
            return redirect(url_for('login'))
        elif cursor.rowcount !=0:
           # global loggedin == true
            return redirect(url_for('loggedin'))
    if request.method == 'GET':
        return ""
    
@app.route('/savedtabs', methods = ['POST', 'GET'])
def showusertabs():
    if request.method == 'POST':
        return "POST"
    if request.method == 'GET':
        return "GET"
    
if __name__ == '__main__':
    app.run(debug = True, port = 8000)
