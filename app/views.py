from flask import render_template
from app import app 
from .request import get_articles

@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    headlines_articles = get_articles('headlines')
    international_news_articles = get_articles('international_news')

    title = 'Home - Welcome to the best and reliable Headlines Scoop Website Online'

    return render_template('index.html', title = title,headlines = headlines_articles,international_news_articles = international_news_articles)

@app.route('/news/<int:news_id>')
def news(news_id):
    """
    View news page function that returns the news details page and its data
    """
    return render_template('news.html',id = news_id)