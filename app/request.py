from app import app
import urllib.request,json
from .models import source
from .models import article
Source=source.Source
Article=article.Article

api_key=app.config['SOURCE_API_KEY']

base_url=app.config['SOURCE_API_BASE_URL']
base1_url=app.config['ARTICLE_API_BASE_URL']

def get_source(category):
    '''
    Function that gets the json response to url request
    '''
    get_source_url=base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data=url.read()
        get_source_response=json.loads(get_source_data)

        source_results= None


        # if get_source_response ['sources']:
        #     source_results_list=get_source_response['sources']

        if get_source_response ['sources']:
            source_results_list=get_source_response['sources']
            source_results= process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''            
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results=[]
    for source in source_list:
        id=source.get('id')
        name=source.get('name')
        description=source.get('description')

        if  id:
            source_Object = Source(id,name,description)
            source_results.append(source_Object)  

    return source_results    

def get_article(id):
    '''
    function that gets json request to the url
    '''
    get_article_url = base1.url.format(id,api_key)

    with urllib.request.urlopen(get_article_url)as url:
        get_article_data=url.read()
        get_article_response=json.loads(get_article_data)

        article_object= None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)

    return article_results        

    def process_results(article_list):
        '''
        Function  that processes the article result and transform them to a list of Objects

        Args:
        article_list: A list of dictionaries that contain article details

        Returns :
        article_results: A list of article objects
        '''

        article_results=[]
        for article in article_list:
            author=article.get('author')
            title=article.get('title')
            description=article.get('description')
            url=article.get('url')
            urlToImage=article.get('urlToImage')
            publishedAt=article.get('publishedAt')
            content=article.get('content')
            
            if  title:
                article_Object = Article(author,title,description,url,urlToImage,publishedAt,content)
                article_results.append(article_Object)  

    return article_results 

        