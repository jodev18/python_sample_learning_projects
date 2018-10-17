
secret_number =8

print("Welcome to my game, muggle!")
while int(input("Enter an integer number and guess what number I've picked for you!(0-10): ")) != secret_number:
    print("No, that's not the number I've picked for you. Try again!")

print("Well done! That's the number I've chosen for you! You are free now.")

