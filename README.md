# movie-title-constructor
Data scrape IMDB to create nominal movie titles and metadata from list of cli URL arguments


## Movie IMDB url-seeker
Takes string input of movie title queries (title and year), input them in imdb search bar and graps URL of first listing
Outputs url_list.csv to be used by the movie_title_constructor.py program

## Movie web-scraper and title constructor
Takes url_list.csv file and constructs title for each URL listing in the given format
#### [MOVIE'S TITLE] (YEAR) [ACTOR FIRSTNAME ACTOR LASTNAME]x3 [MOVIE GENRES]

