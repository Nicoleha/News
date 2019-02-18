from flask import render_template
from app import app
from .request import get_source,get_article

@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    General_cat=get_source("general")
    Business_cat=get_source("business")
    Sports_cat=get_source("sports")
    Entertainment_cat=get_source("entertainment")
    Technology_cat=get_source("technology")

    title='News Highlight Website'
    return render_template('index.html',title=title,general=General_cat,business=Business_cat,sports=Sports_cat,entertainment=Entertainment_cat,technology=Technology_cat)

@app.route('/article/<int:article_id>')
def article(article_id):
    '''
    View source page function that returns the article details page and its data
    '''
    article=get_article(article_id)
    title=f'{article.title}'

    return render_template('article.html',article = article,title=title )

