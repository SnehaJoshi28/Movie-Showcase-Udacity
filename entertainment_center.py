"""This defines the movies and other details """


import media
import fresh_tomatoes

# Creates the movie objects
brave = media.Movie(
    "Brave",
    "A story of a young girl tries to reverse a curse",
    "https://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg",
    "http://www.youtube.com/watch?v=iwZSfVYnGXs")

the_lion_king = media.Movie(
    "The Lion King",
    "As a cub, Simba is forced to leave the jungle after his father is murdered by his wicked uncle.",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcQ2vZQTR7HyXqWbjYYr0HNfAyDLRq7EXogJGAgG0bbM8odQlDLV",
    "https://www.youtube.com/watch?v=zx3LT_G3cIA")

spirited_away = media.Movie(
    "Spirited Away",
    "A sullen 10-year-old girl wanders into a world ruled by gods",
    "https://upload.wikimedia.org/wikipedia/en/d/db/Spirited_Away_Japanese_poster.png",
    "https://www.youtube.com/watch?v=ByXuk9QqQkk")

the_good_dinosaur = media.Movie(
    "The Good Dinosaur",
    "An unlikely friendship between a dinosaur and human boy",
    "https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg",
    "http://www.youtube.com/watch?v=oN5E8DLh10o")

up = media.Movie(
    "Up",
    "78-year old man's lifelong dream of flying with an unexpected boy who stowaway",
    "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
    "https://www.youtube.com/watch?v=pkqzFUhGPJg")

wall_e = media.Movie(
    "Wall-E",
    "A trash compactor robot left in a deserted planet",
    "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
    "https://www.youtube.com/watch?v=alIq_wG9FNk")

# Creates the movie list
movies = [brave, the_lion_king, spirited_away, the_good_dinosaur, up, wall_e]

# calls the method of fresh_tomatoes to display the movies and their other
# details
fresh_tomatoes.open_movies_page(movies)
