from app import app
import urllib.request,json
from .models import source
from .models import article
Source=source.Source
Article=article.Article

api_key=app.config['SOURCE_API_KEY']

base_url=app.config['SOURCE_API_BASE_URL']

def get_source(source):
    '''
    Function that gets the json response to url request
    '''
    get_source_url=base_url.format(source,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data=url.read()
        get_source_response=json.loads(get_source_data)

        source_results= None

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
    for source_item in source_list:
        id=source_item.get('id')
        name=source_item.get('name')

    if  id:
        source_Object = Source(id,name)
        source_results.append(source_Object)  

    return source_results    