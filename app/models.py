class Source:
    """
    Source class to define source objects
    """
    def __init__(self,source,author,title,description,url,urlToImage,publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

class Article:
    '''
    Article class to define article objects
    '''

    def __init__(self, name, author, title,  description, link, image, publishDate):

        self.name = name 
        self.author = author
        self.title = title
        self.description = description
        self.link = link
        self.image = image
        self.publishDate = publishDate        