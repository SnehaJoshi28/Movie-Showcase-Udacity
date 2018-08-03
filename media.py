"""Definition of movie class and its contents"""
import webbrowser

class Movie():
    """
    This is a template for the movies
    
    Args:
        (str) movie_title: title of the movie
        (str) movie_storyline: storyline of the movie
        (str) poster_image: poster of the movie
        (str) trailer_youtube: youtube trailer of the movie
        
    Returns:
        None
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    #This method shows the trailer of the movie through the youtube link
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)