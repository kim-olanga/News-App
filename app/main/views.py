from flask import render_template
# from app import app 
from . import main
from ..request import get_articles,get_sources
from ..models import Source, Article

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_news = get_sources('general')
    business_news = get_sources('business')
    technology_news = get_sources('technology')
    science_news = get_sources('science')
    health_news = get_sources('health')
    entertainment_news = get_sources('entertainment')
    sports_news = get_sources('sports')
    return render_template('index.html',general =general_news, business =business_news,technology = technology_news,
    science = science_news, health = health_news,entertainment = entertainment_news,sports = sports_news)

@main.route('/article/<id>')
def article(id):

    '''
    View news page function that returns the news source page and its data
    '''
    general_news = get_sources('general')
    business_news = get_sources('business')
    technology_news = get_sources('technology')
    science_news = get_sources('science')
    health_news = get_sources('health')
    entertainment_news = get_sources('entertainment')
    sports_news = get_sources('sports')
    article = get_articles(id)
    if article:
        for i in article:
            name = i.name
    else:
         name = ""
        
    return render_template('article.html',general =general_news, business =business_news,technology = technology_news,
    science = science_news, health = health_news,entertainment = entertainment_news,sports = sports_news,article = article,name = name)






# @app.route('/')
# def index():
#     """
#     View root page function that returns the index page and its data
#     """
#     articles = get_articles('articles')
    
#     title = 'Home - Welcome to the best and reliable Headlines Scoop Website Online'

#     return render_template('index.html', title = title,articles = articles)

# @app.route('/source/<int:source_id>')
# def source(source_id):
#     """
#     View source page function that returns the source details page and its data
#     """
#     source = get_source(id)
#     title = f'{source.title}'

#     return render_template('source.html',title = title,source = source)