## SI 506 F18
## Problem Set 9

## Import statements
import requests
import json

## [PROBLEM 1]

# In this problem, you will do some of the same work you did in Problem Set 8 (and some new things), but you will get the data in a different way -- from the iTunes Search API, rather than from a file.

# Use the documentation at https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/ and your knowledge of making requests to REST APIs to write some code (which must fulfill the stated requirements and which should NOT include any function definitions) that does the following things.

# - Make a request to the iTunes Search API for "marvel" (just a search, no other specification) and save the Response in a variable called marvel_response.

baseurl = "https://itunes.apple.com/search"
dic = {'term':'marvel'}
marvel_response = requests.get(baseurl,params=dic)




# - Get the text from the response and load it into a Python object. Save the Python object in a variable called marvel_python_obj.

marveltext = marvel_response.text
marvel_python_obj = json.loads(marvel_response.text)

jsonfile = open('itunes.json', 'w', encoding = "utf-8")
jsonfile.write(marveltext)
jsonfile.close()

# - Use the data in marvel_python_obj to do the following. (You will probably want to write some investigation code first!)

## -- (a) Get the name(s) of the artists of each thing that came up in the search results and save them in a list called artist_titles.

artist_titles = []
short_descriptions = []

for song in marvel_python_obj['results']:
    artist_titles.append(song['artistName'])
    if 'shortDescription' in song:
        short_descriptions.append(song['shortDescription'])



## -- (b) Accumulate all the short descriptions among the results into a list called short_descriptions.
### NOTE that your list should contain a bunch of strings, where each one is a short description of an item in the search, but there will likely be many items in the results that do NOT have a short description.
### HINT: How will you iterate over all the items and only get the value of a short description if it is there at all? How can you make sure not to encounter an error?
### HINT 2: You should NOT use a try/except for this. You can do this with careful thought about how dictionaries work, and an if/else statement -- it's probably much simpler than you think at first!







# [PROBLEM 2]
# Get an OMDb API Key from: http://www.omdbapi.com/apikey.aspx and fill in the OMDB_API_KEY field below:
OMDB_API_KEY = 'd75ed2e1' # 1000 daily limit for free one
# This should happen very quickly, but you must do it before making any requests to OMDB!



# [PROBLEM 3]
## This problem involves using an API with a key authentication -- the OMBD API, which lets you get data from IMDB.

## You can find documentation of the OMDB API at this link: http://www.omdbapi.com/

## The base URL for the OMDB API is the following: http://www.omdbapi.com
omdbbaseurl = 'http://www.omdbapi.com'
omdbdic = {}
omdbdic['apikey'] = OMDB_API_KEY
omdbdic['t'] = 'Black Panther'
## For our purposes (getting information about a specific movie), the parameter 't' is required, and its value must be a real movie title on IMDB.
## The 'apikey' parameter is also required, and its value must be the API key string that you receive by email when you do the previous step of getting an API key -- set in the global variable OMDB_API_KEY above!

## You should write code to make a request to the OMDB API using this baseurl and this set of parameters, for the movie "Black Panther".

omdbresponse = requests.get(omdbbaseurl, params = omdbdic)
omdb_obj = json.loads(omdbresponse.text)

bp_director = omdb_obj['Director']
box_office_bp = omdb_obj['BoxOffice']

## Finally, use the data you got from making this request in order to save:
# -- the value of the director's name ("Ryan Coogler") in the variable bp_director
# -- the value of the box office total for the movie ("$501,105,037") in the variable box_office_bp





# [PROBLEM 4]

## Using the experience (and the code) you have from problem 3, define a function called get_movie_data that accepts as input a string that is a movie title and returns a Python object representing data about that movie.
## You can assume that the program includes a global variable called OMDB_API_KEY at the top.
## You should also be able to invoke this function successfully with ANY movie title that is correct and exists on IMDB.

def get_movie_data(title):
    moviedic = {}
    moviedic['apikey'] = OMDB_API_KEY
    moviedic['t'] = title
    movieresponse = requests.get('http://www.omdbapi.com', moviedic)
    movie_obj = json.loads(movieresponse.text)
    return  movie_obj


## Remember that this function should be able to be invoked in ANY Program with OMDB_API_KEY at the top -- no matter what else is in it, so it should NOT depend on ANY other global variables!




## For example, the following invocations should work AFTER you've defined the function:
## get_movie_data("Batman")
## get_movie_data("Interstellar")
## get_movie_data("Bend it Like Beckham")
