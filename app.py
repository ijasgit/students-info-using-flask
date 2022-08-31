from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        s_name = request.form["name"]
        s_age = request.form["age"]
        s_language = request.form["language"]
        s_preference = request.form["preference"]
        conn=sql.connect("crud.db") #doubt
        cur=conn.cursor() #doubt
        cur.execute("insert into student (NAME,AGE,LANGUAGE,PREFERENCE) value(?,?,?,?)",(s_name,s_age,s_language,s_preference)) #why capital is used,why insert.
        conn.commit()
        return render_template("add_user.html") #what happen when we change the order of code.


@app.route("/edit",methods=["GET","POST"])
def edit_user():
    return render_template("edit_user.html")

if __name__=="__main__":
    app.run(debug=True)