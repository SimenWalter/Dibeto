from flask import Blueprint, render_template, request, session, redirect
import mysql.connector


db = mysql.connector.connect(
 user='root',
 password='69420', 
 host='127.0.0.1',
database='dibeto',
autocommit=True)

cursor = db.cursor(buffered=True)

auth = Blueprint('auth', __name__)

@auth.route('/index')
def index():
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT  * FROM topics")
    data = cursor.fetchall()
    return render_template("home.html", topics=data)

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pass')
        cursor.execute("INSERT INTO users VALUES (NULL, '%s', '%s', NULL)")
        return redirect('/')

@auth.route('/users')
def users():
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM users")
    userdata = cursor.fetchone()
    return render_template("claims.html", users=userdata )


@auth.route('/insert', methods = ['POST','GET'])
def insert():

    if request.method == "POST":
        name = request.form['name']
        text = request.form['text']
        cursor = db.cursor(buffered=True)
        cursor.execute("INSERT INTO topics (topicTitle, topicText) VALUES (%s, %s)", (name, text))
        return redirect("/index")


@auth.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    cursor = db.cursor(buffered=True)
    cursor.execute("DELETE FROM topics WHERE topic_ID=%s", (id_data,))
    db.commit()
    return redirect("/index")



@auth.route('/claims', methods = ['POST','GET'])
def claims():
     cursor.execute("SELECT * FROM claims ")
     data = cursor.fetchall()
     return render_template("claims.html", claims=data )

@auth.route('/insertclaim',  methods = ['POST','GET'])
def insertclaim():

    if request.method == "POST":
        title = request.form['claimtitle']
        text = request.form['claimtext']
        cursor.execute("INSERT INTO claims(claimTitle,claimText) VALUES(%s,%s)", (title, text))
        return redirect("/claims")

@auth.route('/replies', methods = ['POST','GET'])
def replies():
     cursor.execute("SELECT * FROM replies ")
     data = cursor.fetchall()
     return render_template("replies.html", replies=data )

@auth.route('/insertreply',  methods = ['POST','GET'])
def insertreply():

    if request.method == "POST":
        title = request.form['replytitle']
        text = request.form['replytext']
        cursor.execute("INSERT INTO replies(replyTitle, replyText) VALUES(%s,%s)", (title,text))
        return redirect("/replies")



