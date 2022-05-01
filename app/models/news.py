class News:
    """
    News class to define News objects
    """
    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.newsapi.org/t/p/v2/kls25hgfd'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count
        