from app import app
from flask import render_template


# listen for a route at root '/'
# this will be the home page for fishing thing
# need a template/index.html file here to load in render_template func()
@app.route('/')
def index():
    return render_template('public/indexPage.html')


@app.route('/folio')
def folioPage():
    return render_template('public/folioPage.html')
