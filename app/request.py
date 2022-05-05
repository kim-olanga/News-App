# from app import app
import urllib.request,json
from .models import Source,Article
from datetime import datetime

# Source = source.Source

def configure_request(app):
    global api_key,base_url,article_url,top_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['SOURCE_API_BASE_URL']
    article_url = app.config['ARTICLE_API_BASE_URL']
    
def get_sources(category):
    """
    Function that gets the json response to our url requests
    """
    get_sources_url = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey=1c2e4612d4764934ad588e621b350633'.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    """
    Function that processes source results and transform them to a list of objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns:
        source_results: A list of source objects
    """
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')        
        name= source_item.get('name')
        category = source_item.get('category')
        source_object= Source(id,name,category)
        source_results.append(source_object)
        
    return source_results

def get_articles(id):
    get_article_url = 'https://newsapi.org/v2/everything?q={}&apikey=1c2e4612d4764934ad588e621b350633'.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        
        if article_details_response['articles']:
            article_results_list = article_details_response['articles']

        article_results = []
        if article_details_response["totalResults"] > 0:

            for article_item in article_results_list:
                name = article_item.get('source').get('name')
                author = article_item.get('author')
                title = article_item.get('title')
                description = article_item.get('description')
                url = article_item.get('url')
                urlToImage = article_item.get('urlToImage')
                pdate = article_item.get('publishedAt')
                
                publishedAt = datetime.strptime(pdate, '%Y-%m-%dT%H:%M:%SZ').date()

                if urlToImage != "null":
                    article_object = Article(name,author,title,description,url,urlToImage,publishedAt)
                    article_results.append(article_object)
        else:
            return
    return article_results