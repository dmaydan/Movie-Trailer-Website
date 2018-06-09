import media
import fresh_tomatoes
# Create instances of Movie class
toy_story = media.Movie(
    "Toy Story",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

toy_story_2 = media.Movie(
    "Toy Story 2",
    "https://upload.wikimedia.org/wikipedia/en/c/c0/Toy_Story_2.jpg",
    "https://www.youtube.com/watch?v=xNWSGRD5CzU")

toy_story_3 = media.Movie(
    "Toy Story 3",
    "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
    "https://www.youtube.com/watch?v=JcpWXaA2qeg")
# Store Movie instances in list
movies = [toy_story, toy_story_2, toy_story_3]
# Generate and open static web page that displays movies
fresh_tomatoes.open_movies_page(movies)
