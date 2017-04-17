import fresh_tomatoes
import media


# Creating variables for movies array
rushmore = media.Movie("Rushmore",
                       "A teenager becomes friends with rich industrialist \
                       and they both fall for an elementary school teacher",
                       "https://goo.gl/NCuXan",
                       "https://youtu.be/W0Lc-5jOhhY")

new_hope = media.Movie("Star Wars",
                       "An epic space opera about good vs. evil",
                       "https://goo.gl/j75Jtx",
                       "https://youtu.be/vZ734NWnAHA")

be_kind_rewind = media.Movie("Be Kind Rewind",
                             "A community comes together to save a local \
                             business",
                             "https://goo.gl/i5fGxV",
                             "https://youtu.be/J7C8nHAAs70")

lost_in_translation = media.Movie("Lost in Translation",
                                  "Two strangers frind friendship in a far \
                                  away place",
                                  "https://goo.gl/ElB3nu",
                                  "https://youtu.be/W6iVPCRflQM")

amelie = media.Movie("Amelie",
                     "A shy waitress changes the lives of the people around \
                     her",
                     "https://goo.gl/TBLEY0",
                     "https://youtu.be/HUECWi5pX7o")

eternal_sunshine = media.Movie("Eternal Sunshine",
                               "When a relationship goes bad, a couple decides \
                               to have their memories of each other erased",
                               "https://goo.gl/yKU3vv",
                               "https://youtu.be/0zFywiAh7N0")

# Array with movie variables
movies = [rushmore,
          new_hope,
          be_kind_rewind,
          lost_in_translation,
          amelie,
          eternal_sunshine]
fresh_tomatoes.open_movies_page(movies)
