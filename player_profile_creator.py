import profile


print("Welcome to the player profile creator")
print("We will create a player profile for you. Please answer these few following questions.")
name = input("First question, what is your name?")
age = input("Second question, how old are you?")
hobby = input("Third question, what is your hobby?")
favorite_game = input("Fourth question, what is your favorite game?")
favorite_brand = input("Fifth question, what is your favorite brand?")

profile = {
    "Name": name,
    "Age": age,
    "Hobby": hobby,
    "Favorite Game": favorite_game,
    "Favorite Brand": favorite_brand
}

print("Thank you for answering the questions. Here is your player profile:")
for key, value in profile.items():
    print(key, ":", value)
