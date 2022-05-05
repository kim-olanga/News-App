class Sources:
    """
    News class to define News objects
    """
    def __init__(self,id,title,author,url,urlToImage,description,PublishedAt):
        self.id = id
        self.title = title
        self.author = author
        self.url = url
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = PublishedAt
        