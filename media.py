class Movie():
    """A glorious form of entertainment.

    Attributes:
        title (str):  The title of the movie
        poster_image_url (str):  The URL of the poster image of the movie
        trailer_youtube_url:  The youtube URL of the movie
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Args:
            movie_title (str):  The title of the movie
            poster_image (str):  The URL of the poster image of the movie
            trailer_youtube (str):  The youtube URL of the movie
         """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube