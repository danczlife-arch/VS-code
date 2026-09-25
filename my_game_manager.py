
print("Welcome to the Game Manager! Here you can manage your favorite games.")
question = input("Do you want to add a game to your library? yes/no: ")
if question == "yes":
    question = input("Please enter the name of the game you want to add: ")
else:
    print("Your game library is empty")

print(f"You added {question} to your game library.")
Library = [question]
ask = input("Do you want to add more games? yes/no: ")
if ask == "yes":
    new_game = input("Please enter the name of the game you want to add: ")
    print(f"Your updated game library: {Library}")
    Library = [question, new_game]
else:
    print("No more games added.")
remove_game = input("Do you want to remove a game from your library? yes/no: ")
if remove_game == "yes":
    game_to_remove = input("Please enter the name of the game you want to remove: ")
    if game_to_remove in Library:
        Library.remove(game_to_remove)
        print(f"{game_to_remove} has been removed from your library.")
    else:
        print(f"{game_to_remove} is not in your library.")
else:
    print("No games removed.")
quetsion = input("Do you want to see your game library? yes/no: ")
if quetsion == "yes":
    print(f"Your game library: {Library}") 
else:
    print("Okay, you can check your library later! Bye!")