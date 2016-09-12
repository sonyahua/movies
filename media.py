import webbrowser

class Movie():
        """This class provides a way to store movie-related information"""

        VALID_RATINGS = ["G", "PG", "PG-13", "R"]

        def __init__(self, title, year, movie_storyline, poster_image, trailer_youtube):
               self.title=title
               self.year=year
               self.storyline=movie_storyline
               self.poster_image_url=poster_image
               self.trailer_youtube_url=trailer_youtube

        def play_trailer(self):
               """Plays trailer based on Youtube URL provided"""
               webbrowser.open(self.trailer_youtube_url)

        def printer(self, msg):
                print(self.jeff + msg)

# remember to indent for nested functions
# each instance method takes first arg as self

