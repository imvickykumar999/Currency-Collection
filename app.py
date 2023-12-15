
from flask import (Flask,
    render_template,
    request,redirect,
    url_for,flash
)

import sqlite3 as sql
from werkzeug.utils import secure_filename
import os, random, secrets

app=Flask(__name__)
secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key

UPLOAD_FOLDER ="static/files"
FILE_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_extensions(file_name):
    return '.' in file_name and file_name.rsplit('.',1)[1].lower() in FILE_EXTENSIONS
           
@app.route("/fileUpload",methods=['GET','POST'])
def fileUpload():
    if request.method=='POST':
        if 'file' not in request.files:
            flash('No file part','danger')
            
        file = request.files['file']
        if file.filename == '':
            flash('No file selected','danger')
            
        if file and allowed_extensions(file.filename):
            filename, file_extension = os.path.splitext(file.filename)
            new_filename = secure_filename(filename+str(random.randint(10000,99999))+"."+file_extension)
            file.save(os.path.join(UPLOAD_FOLDER, new_filename))   
            
            flash(file.filename+' Uploaded Successfully','success')
        return redirect(url_for("index"))
    return render_template('fileUpload.html')

@app.route("/")
@app.route("/index")
def index():

    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()

    cur.execute("select * from users")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

@app.route("/add_user",methods=['POST','GET'])
def add_user():

    if request.method=='POST':
        uname=request.form['uname']
        contact=request.form['contact']

        con=sql.connect("db_web.db")
        cur=con.cursor()

        cur.execute("insert into users(UNAME,CONTACT) values (?,?)",(uname,contact))
        con.commit()

        flash('Currency Added','success')
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<string:uid>",methods=['POST','GET'])
def edit_user(uid):

    if request.method=='POST':
        uname=request.form['uname']
        contact=request.form['contact']

        con=sql.connect("db_web.db")
        cur=con.cursor()

        cur.execute("update users set UNAME=?,CONTACT=? where UID=?",(uname,contact,uid))
        con.commit()

        flash('Currency Updated','success')
        return redirect(url_for("index"))
    
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()

    cur.execute("select * from users where UID=?",(uid,))
    data=cur.fetchone()
    return render_template("edit_user.html",datas=data)
    

@app.route("/delete_user/<string:uid>",methods=['GET'])
def delete_user(uid):
    con=sql.connect("db_web.db")

    cur=con.cursor()
    cur.execute("delete from users where UID=?",(uid,))
    con.commit()

    flash('Currency Deleted','warning')
    return redirect(url_for("index"))
    
if __name__=='__main__':
    app.run(debug=True)
