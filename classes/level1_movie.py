# Q10: Create two Movie objects and display their details.
class Movie:
    def __init__(self, name, hero, heroine, rating):
        self.name = name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating

movie1 = Movie("Dream", "Arun", "Meena", 4.5)
movie2 = Movie("Action", "Vijay", "Tara", 4.0)
print(movie1.name, movie1.hero, movie1.heroine, movie1.rating)
print(movie2.name, movie2.hero, movie2.heroine, movie2.rating)
