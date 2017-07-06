from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user={'nickname':'Karthik'} # Fake for now
    posts = [
        {
            'author': {'nickname':'Kaushik'},
            'body': 'Chennai is awesome!!'
        },
        {
            'author': {'nickname': 'Vignesh'},
            'body' : 'Dei! mama pesaren da'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)