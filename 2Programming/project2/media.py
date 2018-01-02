class Movie():
    """Movie Class for initializing movie's instances"""

    def __init__(self, movie_name, year, movie_poster, movie_trailer):
        """ Movie class constructor method to initialize instance
        with movie's title, release year, poster image and trailer """
        self.title = movie_name
        self.year = year
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
