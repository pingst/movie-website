import webbrowser


class Movie():
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        # Initializing instance variables for movie title, storyline, image,
        # and trailer which we want class Movie to remember
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Instance method to open webbrowser to open youtube trailer
        webbrowser.open(self.trailer_youtube_url)
