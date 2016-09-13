# movies
As part of [Udacity's Full-Stack Web Developer program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004), create a webpage, powered by Python, featuring my most recent favorite movies

##Instructions: How to Launch Webpage

Before attempting below instructions, please ensure [python is installed](https://www.python.org/downloads/) on your computer and your python version is [appended to your path](http://stackoverflow.com/questions/6318156/adding-python-path-on-windows-7).

1. Download and save all files on your local drive.
2. Open a command prompt:
    - For Windows 8 onwards: Start --> Run (or type Win+R) --> `cmd.exe` --> OK
    - For Mac: Open Finder --> Select Applications --> Utilities --> Doubleclick on Terminal
3.  Within terminal shell, using `cd`, navigate to where the repository files are stored. For example:
    - `cd  c:/users/sonya/documents/python/movies`
4.  Run the statement `python movies_data.py` to execute the script file
    - If you get the following message:
    ```'python' is not recognized as an internal or external command, operable program or batch file.```
    ... check to make sure python is installed and [appended to your path](http://stackoverflow.com/questions/6318156/adding-python-path-on-windows-7).
5.  Web page will launch on your default web browser.

##API

The [Movie Database API](https://www.themoviedb.org/documentation/api) is utilized to pull in movie information from selected movies. In this project, the following fieldsets is requested from API. 

|API Fieldsets              |
| ------------------------- |
|Movie title                |   
|Release date (year)        |   
|Synopsis                   |   
|Poster URL                 |   
|Official Movie Trailer URL |  

##Movie Selection Customization

Customize the movie selection by:

1. Search and record the movie ID's of the movies in [The Movie Database website](https://www.themoviedb.org/).
2. Based on your search, Alter the movie ID's within `movies_data.py` and variables in below section of code. Change the movie ID's and variable names based on your movie titles. (i.e. <font-color="red">`guardians_of_galaxy_id = '118340'`</font-color>). Update the `list_of_movies` array to include new variables. For example, `guardians_of_galaxy_id` is added to the following array:

    ```python 
    MovieNames = [edge_of_tomorrow_id, furious_7_id, joy_id, 
                      star_trek_beyond_id, young_adult_id, whiplash_id, guardians_of_galaxy_id]
    ```

Customizable movie ID variables:
```python
def search_movie_info():
    """Fetches movie info from Movie Database"""
    
    # tmdb IDs for selected movies
    edge_of_tomorrow_id = '137113'
    furious_7_id = '168259'
    joy_id = '274479'    #tmdb's movie ID for the move Joy
    star_trek_beyond_id = '188927'
    whiplash_id ='244786'
    young_adult_id ='57157'

    # Store movie IDs in an array/list
    MovieNames = [edge_of_tomorrow_id, furious_7_id, joy_id, star_trek_beyond_id,young_adult_id,whiplash_id]
```     