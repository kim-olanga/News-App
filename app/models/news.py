class News:
    """
    News class to define News objects
    """
    def __init__(self,articles,author,title,description,poster,publishedAt):
        self.articles = articles
        self.author = author
        self.title = title
        self.description = description
        self.poster = 'https://urlToImage/'+ poster
        self.publishedAt = publishedAt        