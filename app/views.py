from flask import render_template
from app import app
from .request import get_source

@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    Bitcoin=get_source("bitcoin")
    Business=get_source("business")
    title='News Highlight Website'
    return render_template('index.html',title=title,bitcoin=Bitcoin,business=Business)

@app.route('/article/<int:source_id>')
def article(source_id):
    '''
    View source page function that returns the movie details page and its data
    '''
    return render_template('source.html',id = source_id )

