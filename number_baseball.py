# Number Baseball


from random import randint


def generate_numbers(): # Select 3 random numbers
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("selected 3 different numbers between 0 and 9 in random order.\n")
    return numbers

def take_guess(): # User input numbers
    print("Enter three numbers one by one.")

    guess = []

    while len(guess) < 3:
        new_num = int(input("Enter No.{}: ".format(len(guess) + 1)))

        if new_num < 0 or new_num > 9:
            print("The number is out of range. Please enter again.")
        elif new_num in guess:
            print("The number is a duplicate. Please enter again.")
        else:
            guess.append(new_num)

    return guess

def get_score(guesses, solution): # Count strikes and balls
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count

ANSWER = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break

print("Congratulations! You have guessed all three numbers correctly, in {} attempts.".format(tries))







