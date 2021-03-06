from flask import render_template
from app import app 

@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Home - Welcome to the best and reliable Headlines Scoop Website Online'
    return render_template('index.html', title = title)

@app.route('/news/<int:news_id>')
def news(news_id):
    """
    View news page function that returns the news' details page and its data
    """
    return render_template('news.html',id = news_id)