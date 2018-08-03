"""This defines the movies and other details """


import media
import fresh_tomatoes

#creates the movie objects
brave = media.Movie("Brave","A story of a young girl tries to reverse a curse caused by disobeying ancient custom, only to find out what real bravery means", "https://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg","http://www.youtube.com/watch?v=iwZSfVYnGXs")

the_lion_king = media.Movie("The Lion King" ,"As a cub, Simba is forced to leave the jungle after his father is murdered by his wicked uncle. Years later, he returns with friends to face his nemesis who harmed his family." ,"http://t1.gstatic.com/images?q=tbn:ANd9GcQ2vZQTR7HyXqWbjYYr0HNfAyDLRq7EXogJGAgG0bbM8odQlDLV","https://www.youtube.com/watch?v=zx3LT_G3cIA")

spirited_away = media.Movie("Spirited Away" ,"During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts." ,"https://upload.wikimedia.org/wikipedia/en/d/db/Spirited_Away_Japanese_poster.png","https://www.youtube.com/watch?v=ByXuk9QqQkk")

the_good_dinosaur = media.Movie("The Good Dinosaur" ,"An unlikely friendship between a dinosaur and human boy, who discover whole new world " ,"https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg","http://www.youtube.com/watch?v=oN5E8DLh10o")

up = media.Movie("Up" ,"78-year old man's lifelong dream of flying with an unexpected boy who stowaway " ,"https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg", "https://www.youtube.com/watch?v=pkqzFUhGPJg")

wall_e = media.Movie("Wall-E" ,"A trash compactor robot left in a deserted planet, who travels across the galaxy for the love with a probe sent " ,"https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg","https://www.youtube.com/watch?v=alIq_wG9FNk")

#Creates the movie list
movies = [brave,the_lion_king,spirited_away,the_good_dinosaur,up,wall_e]

#calls the method of fresh_tomatoes to display the movies and their other details
fresh_tomatoes.open_movies_page(movies)