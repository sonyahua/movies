import json
import urllib2
import media
import fresh_tomatoes

# My API key from Movie Database API
API_KEY = '69f77b122c6932f085d9c8e992fe70ad'


def search_movie_info():
    """The function fetches movie info from Movie Database API based on movie ID of selected movies.
    Next it populates an array called listOfMovies with movie info."""
    
    # tmdb IDs for selected movies
    edge_of_tomorrow_id = '137113'
    furious_7_id = '168259'
    joy_id = '274479'    #tmdb's movie ID for the move Joy
    star_trek_beyond_id = '188927'
    whiplash_id ='244786'
    young_adult_id ='57157'

    # Store movie IDs in an array/list
    MovieNames = [edge_of_tomorrow_id, furious_7_id, joy_id, star_trek_beyond_id, young_adult_id, whiplash_id]
        
    listOfMovies = []   # create an empty array that will be populated with below info

    # connect with API for each movie id and retreive title, year, storyline, poster path, and trailer path
    for movie_id in MovieNames:
        connection=urllib2.urlopen("https://api.themoviedb.org/3/movie/" + movie_id + "?api_key=" + API_KEY + "&append_to_response=trailers")
        output = connection.read()
        json_output = json.loads(output)

        title = (json_output['title'])
        year = (json_output['release_date'])[:4]
        info = (json_output['overview'])[:155] + '..'
        poster_path = ("https://image.tmdb.org/t/p/w396" + 
                        (json_output['poster_path']))   #creating the full url for poster image
        trailer_path = ("https://www.youtube.com/watch?v=" + (json_output['trailers']['youtube'][0]['source']))
        
        # create an instance called movie of Movie class
        movie = media.Movie(title, year, info, poster_path, trailer_path)
        
        # Populate the array with the movie info
        listOfMovies.append(movie)
        
    # Print out data in listofMovies array
    for movie in listOfMovies:
        print(movie.title)
        print(movie.year)
        print(movie.storyline)
        print(movie.poster_image_url)
        print(movie.trailer_youtube_url)

    # create a webpage of movies
    fresh_tomatoes.open_movies_page(listOfMovies)

#run the function
search_movie_info()
