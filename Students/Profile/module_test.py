name = input("What is your name? ")

def create_greeting(name):
	"""Create a friendly greeting, with a fallback for blank input."""
	name = name.strip()
	if not name:
		return "Hello!"
	return f"Hello, {name}!"


print(create_greeting(name))