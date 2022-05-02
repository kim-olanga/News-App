from app import app
import urllib.request,json
from .models import news

News = news.News

api_key = app.config['NEWS_API_KEY']

base_url = app.config['NEWS_API_BASE_URL']

def get_articles(category):
    """
    Function that gets the json response to our url requests
    """
    get_articles_url = 'https://newsapi.org/v2/everything?q={}&apikey=ba958fb1a45945d59f5dcedc69137c25'.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        news_results = None

        if get_articles_response['articles']:
            news_results_list = get_articles_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    """
    Function that processes news results and transform them to a list of objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns:
        news_results: A list of news objects
    """
    news_results = []
    for news_item in news_list:
        articles = news_item.get('article')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        poster = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        if poster:
            news_object = News(articles,author,title,description,poster,publishedAt)
            news_results.append(news_object)

    return news_results