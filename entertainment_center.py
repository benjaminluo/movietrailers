import media
import fresh_tomatoes
# __init__ gets called
# self is toy_story
# movie_title is "Toy Story"
# movie_storyline is "A story of a boy..."
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
tron = media.Movie("Tron",
                   "Digital frontier for Sam Flynn",
                   "http://cdn.collider.com/wp-content/uploads/tron_legacy_final_poster_hi-res_01.jpg",
                   "https://www.youtube.com/watch?v=L9szn1QQfas")
movies = [toy_story, avatar, tron]
fresh_tomatoes.open_movies_page(movies)
