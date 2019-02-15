from app import app
import urllib.request,json
from .models import source
Source=source.Source

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

        if get_movies_response ['results']:
            source_results_list=get_source_response['results']
            source_results= process_results[source_results_list]

            return source_results