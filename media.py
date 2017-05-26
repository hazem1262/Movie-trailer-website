# this is the class movie
class Movie():
    """This is the movie class to add title,storyline,poster image
     & the trailer of a movie"""
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title  # adding the movie title
        self.poster_image_url = poster_image  # adding the poster image url
        self.trailer_youtube_url = trailer_youtube  # adding the trailer url

