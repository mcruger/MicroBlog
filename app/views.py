from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Carl'} #mock user obj
    posts = [ #mock posts obj
        {
            'author': {'nickname': 'Jack'},
            'body': 'Good surf today brah!'
        },
        {
            'author': {'nickname': 'Sally'},
            'body': 'Guardians of the Galaxy. So good.'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

