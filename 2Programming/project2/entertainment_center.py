import media
import fresh_tomatoes

'''Programme entry module, which will initializing all the movies' instances'''

# Youth movie:
# movie title, release year, poster image and trailer
youth = media.Movie(
        "YOUTH",
        2017,
        "https://upload.wikimedia.org/wikipedia/en/3/34/"
        "Bloom_of_Youth.jpg",
        "https://www.youtube.com/watch?v=m-oJEoSZ2zU")

# I Am Not Madame Bovary movie:
# movie title, release year, poster image and trailer
madame_bovary = media.Movie(
    "I Am Not Madame Bovary",
    2016,
    "https://upload.wikimedia.org/wikipedia/en/3/3a/"
    "I_Am_Not_Madame_Bovary_poster.jpeg",
    "https://www.youtube.com/watch?v=4iQXpdcX33A")

# Personal Tailor movie:
# movie title, release year, poster image and trailer
personal_tailer = media.Movie(
    "Personal Tailor",
    2013,
    "https://upload.wikimedia.org/wikipedia/en/8/82/"
    "Personal_Tailor_poster.jpg",
    "https://www.youtube.com/watch?v=k1lePkzAlMw")

# Back to 1942 movie:
# movie title, release year, poster image and trailer
back_to_1942 = media.Movie(
    "Back to 1942",
    2012,
    "https://upload.wikimedia.org/wikipedia/en/7/73/"
    "Back_to_1942.jpg",
    "https://www.youtube.com/watch?v=aRy5PJWL1T4")

# If You Are the One 2 movie:
# movie title, release year, poster image and trailer
if_you_are_the_one_2 = media.Movie(
    "If You Are the One 2",
    2010,
    "https://upload.wikimedia.org/wikipedia/en/7/72/"
    "If_You_Are_the_One_2_poster.jpg",
    "https://www.youtube.com/watch?v=5c7PyRNgvJQ")

# Aftershock movie:
# movie title, release year, poster image and trailer
aftershock = media.Movie(
    "Aftershock",
    2010,
    "https://upload.wikimedia.org/wikipedia/en/a/af/"
    "Aftershock.jpg",
    "https://www.youtube.com/watch?v=k18YlPyIjZM")

# If You Are the One movie:
# movie title, release year, poster image and trailer
if_you_are_the_one = media.Movie(
    "If You Are the One",
    2008,
    "https://upload.wikimedia.org/wikipedia/en/7/76/"
    "If_You_Are_The_One.jpg",
    "https://www.youtube.com/watch?v=ODN9Ep24KgU")

# Assembly movie:
# movie title, release year, poster image and trailer
assembly = media.Movie(
    "Assembly",
    2007,
    "https://upload.wikimedia.org/wikipedia/en/b/ba/"
    "Assembly_Poster.jpg",
    "https://www.youtube.com/watch?v=5VG1DrvN4rE")

# The Banquet movie:
# movie title, release year, poster image and trailer
the_banquet = media.Movie(
    "The Banquet",
    2006,
    "https://upload.wikimedia.org/wikipedia/en/a/a0/"
    "Thebanquetposter.jpg",
    "https://www.youtube.com/watch?v=FbQMF-xF8JU")

# A World Without Thieves movie:
# movie title, release year, poster image and trailer
a_world_without_thieves = media.Movie(
    "A World Without Thieves",
    2004,
    "https://upload.wikimedia.org/wikipedia/en/c/c9/"
    "A_World_Without_Thieves.jpg",
    "https://www.youtube.com/watch?v=qY4YWLmgFE8")

# Cell Phone movie:
# movie title, release year, poster image and trailer
cell_phone = media.Movie(
    "Cell Phone",
    2003,
    "https://upload.wikimedia.org/wikipedia/en/1/1c/"
    "Cell_Phone_movie_poster.jpg",
    "https://www.youtube.com/watch?v=QCDg-elqc3k")

# Array of above movies which will be used by the fresh tomatoes module
movies = [youth,
          madame_bovary,
          personal_tailer,
          back_to_1942,
          if_you_are_the_one_2,
          aftershock,
          if_you_are_the_one,
          assembly,
          the_banquet,
          a_world_without_thieves,
          cell_phone
          ]

# The method in fresh tomato module to generate HTML file, 
# and open in web browser with above movies.
fresh_tomatoes.open_movies_page(movies)
