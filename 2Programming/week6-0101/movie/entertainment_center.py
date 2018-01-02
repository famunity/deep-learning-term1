import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Toy Story Story line",
                        "csdf",
                        "cdas")

avatar = media.Movie("Avatar",
                     "Avatar Story line",
                     "https://cdn.movieweb.com/img.teasers.posters/FIsT9wwulpYIwu_369_a/Avatar-2.jpg",
                     "https://www.youtube.com/watch?v=vGNGGBzaNQ0")

movies = [toy_story, avatar]

fresh_tomatoes.open_movies_page(movies)

print media.Movie.__name__
print media.Movie.__module__