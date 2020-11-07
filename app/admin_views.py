from app import app
from flask import render_template, redirect, url_for, request, session


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        session.permanent = False
        user = request.form["username"]
        session["user"] = user
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            return redirect(url_for("user"))
        return render_template('admin/login2.html')


@app.route('/user')
def user():
    if "user" in session:
        user = session['user']
        return redirect(url_for("index"))
    else:
        return redirect(url_for("logout"))


@app.route('/logout')
def logout():
    session.pop("user", None)
    return render_template("admin/logout.html")
