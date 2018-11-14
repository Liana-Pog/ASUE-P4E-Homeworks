import random 
generated_number = random.randint(1,100)

num_of_guesses = 0
guessed_number = 0

while int(guessed_number) != generated_number:
	guessed_number = input("Your guess: ")

	if guessed_number == "exit":
		break

	num_of_guesses += 1

	if int(guessed_number) > generated_number:
		print("Enter a lower number")
	elif int(guessed_number) < generated_number:
		print("Enter a higer number")
else:
	print("Congratualations")
	print("You guessed it in {} steps" .format(num_of_guesses))

