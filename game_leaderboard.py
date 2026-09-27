players = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [1500, 2000, 1800, 2200, 1700]
scores.sort(reverse=True)

for i in range(len(scores)):
    print(i + 1, ".", players[i], "-", scores[i])
