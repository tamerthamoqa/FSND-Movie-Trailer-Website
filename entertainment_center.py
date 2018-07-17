from media import Movie
from fresh_tomatoes import open_movies_page

def ready_movies():
    """Instantiates media.Movie objects and returns a list of those objects.
    Args:
        None
    Returns:
          list of media.Movie objects
     """
    troy = Movie(movie_title="Troy",
                       poster_image="https://upload.wikimedia.org/wikipedia/en/b/b8/Troy2004Poster.jpg",
                       trailer_youtube="https://www.youtube.com/watch?v=znTLzRJimeY")

    kingdom_of_heaven = Movie(movie_title="Kingdom of Heaven",
                                    poster_image="https://upload.wikimedia.org/wikipedia/en/9/9e/KoHposter.jpg",
                                    trailer_youtube="https://www.youtube.com/watch?v=moNH4N44D28")

    warrior = Movie(movie_title="Warrior",
                          poster_image="https://upload.wikimedia.org/wikipedia/en/e/e3/Warrior_Poster.jpg",
                          trailer_youtube="https://www.youtube.com/watch?v=I5kzcwcQA1Q")

    pulp_fiction = Movie(movie_title="Pulp Fiction",
                               poster_image="https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                               trailer_youtube="https://www.youtube.com/watch?v=s7EdQ4FqbhY")

    fight_club = Movie(movie_title="Fight Club",
                             poster_image="https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                             trailer_youtube="https://www.youtube.com/watch?v=SUXWAEX2jlg")

    the_matrix = Movie(movie_title="The Matrix",
                             poster_image="https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                             trailer_youtube="https://www.youtube.com/watch?v=vKQi3bBA1y8")

    the_dark_knight = Movie(movie_title="The Dark Knight",
                                  poster_image="https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                                  trailer_youtube="https://www.youtube.com/watch?v=vKQi3bBA1y8" )

    whiplash = Movie(movie_title="Whiplash",
                           poster_image="https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
                           trailer_youtube="https://www.youtube.com/watch?v=7d_jQycdQGo")

    dredd = Movie(movie_title="Dredd",
                        poster_image="https://upload.wikimedia.org/wikipedia/en/1/16/Dredd2012Poster.jpg",
                        trailer_youtube="https://www.youtube.com/watch?v=qv-6dNqqnMA")

    ai_artificial_intelligence = Movie(movie_title="A.I. Artificial Intelligence",
                                             poster_image="https://upload.wikimedia.org/wikipedia/en/e/e6/AI_Poster.jpg",
                                             trailer_youtube="https://www.youtube.com/watch?v=_19pRsZRiz4" )

    watchmen = Movie(movie_title="Watchmen",
                           poster_image="https://upload.wikimedia.org/wikipedia/en/b/bc/Watchmen_film_poster.jpg",
                           trailer_youtube="https://www.youtube.com/watch?v=PVjA0y78_EQ" )

    the_rock = Movie(movie_title="The Rock",
                           poster_image="https://upload.wikimedia.org/wikipedia/en/8/82/The_Rock_%28movie%29.jpg",
                           trailer_youtube="https://www.youtube.com/watch?v=jGVJx5mOtL8")

    movies = [troy, kingdom_of_heaven, warrior, pulp_fiction, fight_club, the_matrix,
              the_dark_knight, whiplash, dredd, ai_artificial_intelligence,
              watchmen, the_rock]

    return movies

# Instantiating Movie objects
movies = ready_movies()
# Creating output HTML file with movies list
open_movies_page(movies=movies)