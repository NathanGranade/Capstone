from flask import Flask
from views import views
from flask import Flask, flash, render_template, request, redirect, url_for, session
from flask_dropzone import Dropzone
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import random
import MySQLdb

import os

from transcriber import transcribe

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(views, url_prefix="/")
app.config.update(
   UPLOADED_PATH = os.path.join(basedir, 'uploads'),
   DROPZONE_MAX_FILE_SIZE = 1024,
   DROPZONE_TIMEOUT = 5*60*1000
)

dropzone = Dropzone(app)
    
app.config['MYSQL_HOST'] = "sql9.freemysqlhosting.net"
app.config['MYSQL_USER'] = "sql9591604"
app.config['MYSQL_PASSWORD'] = "VGFGb1Ka2c"
app.config['MYSQL_DB'] = "sql9591604"

mysql = MySQL(app)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/app', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        Tscript = transcribe(f.filename)
        session["var"] = Tscript
        songnotes = Tscript
        songID = random.randrange(1000)
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO Tabs (Tablature, idSong) VALUES(%s,%s)''',(songnotes, songID))
        mysql.connection.commit()
        cursor.close()
    return render_template('app.html')

@app.route('/display')
def display():
        if "var" in session:
            var = session["var"]
            return render_template('display.html', var = var)
        else:
            return render_template('display.html', var ='no data in session')

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

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
     
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        idUser = random.randrange(100)
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO Users (Email,Username,Password,idUser) VALUES(%s,%s,%s,%s)''',(email,username,password,idUser))
        mysql.connection.commit()
        cursor.close()
    if email and username and password:
        return render_template('login.html', d = "USER REGISTERED")
    else:
        return render_template('login.html', d = "Please fill out all forums.")


if __name__ == '__main__':
    app.run(debug = True, port = 8000)
