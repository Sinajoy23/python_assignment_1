fruits = ['apple', 'watermelon', 'cherry', 'orange', 'elderberry']
print("Raw list:", fruits)
fruits.append('banana')  # Add
print("After adding a fruit:", fruits)
fruits.remove('apple')  # Remove
print("After removing a fruit:", fruits)
print("Reversed list:", fruits[::-1])
print("")
print("")
# Task 2
info = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
info["favorite color"] = "pink"
info["city"] = "Madrid"
print("")
print("")
print("Keys:")
for key in info.keys():
    print(key)

print("\nValues:")
for value in info.values():
    print(value)

print("")
print("")
#Task 3
favorite_movies = ('Mission Impossible', 'Bohemian Rhapsody', 'New Jack City', 'The Matrix', 'The Shawshank Redemption')
print("Favorite Movies:", favorite_movies)

# Uncommenting the next line will error out because tuples are immutable
#favorite_movies[0] = 'Avatar'

print("Oops! Tuples cannot be changed.")
print("Length of tuple:", len(favorite_movies))




