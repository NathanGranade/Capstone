from flask import Flask
from views import views
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import random
import MySQLdb

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")
    
app.config['MYSQL_HOST'] = "sql9.freemysqlhosting.net"
app.config['MYSQL_USER'] = "sql9591604"
app.config['MYSQL_PASSWORD'] = "VGFGb1Ka2c"
app.config['MYSQL_DB'] = "sql9591604"

mysql = MySQL(app)

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        idUser = random.randrange(20)
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO Users (Email,Username,Password,idUser) VALUES(%s,%s,%s,%s)''',(email,username,password,idUser))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
