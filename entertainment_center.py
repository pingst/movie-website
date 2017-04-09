import fresh_tomatoes
import media

rushmore = media.Movie("Rushmore",
                       "A teenager becomes friends with rich industrialist \
                       and they both fall for an elementary school teacher",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/Rushmoreposter.png/220px-Rushmoreposter.png",
                       "https://www.youtube.com/watch?v=W0Lc-5jOhhY")

new_hope = media.Movie("Star Wars",
                       "An epic space opera about good vs. evil",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg",
                       "https://www.youtube.com/watch?v=vZ734NWnAHA")

be_kind_rewind = media.Movie("Be Kind Rewind",
                             "A community comes together to save a local business",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Be_Kind_Rewind_poster.jpg/220px-Be_Kind_Rewind_poster.jpg",
                             "https://www.youtube.com/watch?v=J7C8nHAAs70")

lost_in_translation = media.Movie("Lost in Translation",
                                  "Two strangers frind friendship in a faw away place",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Lost_in_Translation_poster.jpg/220px-Lost_in_Translation_poster.jpg",
                                  "https://www.youtube.com/watch?v=W6iVPCRflQM")

amelie = media.Movie("Amelie",
                     "A shy waitress changes the lives of the people around her",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Amelie_poster.jpg/220px-Amelie_poster.jpg",
                     "https://www.youtube.com/watch?v=HUECWi5pX7o")

eternal_sunshine = media.Movie("Eternal Sunshine",
                               "When a relationship goes bad, a couple decides \
                               to have their memories of each other erased",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg/220px-Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                               "https://www.youtube.com/watch?v=0zFywiAh7N0")

movies = [rushmore, new_hope, be_kind_rewind, lost_in_translation, amelie, eternal_sunshine]
fresh_tomatoes.open_movies_page(movies)
