from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    title='News Highlight Website'
    return render_template('index.html',title=title)

@app.route('/source/<int:source_id>')
def source(source_id):
    '''
    View source page function that returns the movie details page and its data
    '''
    return render_template('source.html',id = source_id )