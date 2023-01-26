from functions import generate_random_secret_number, check_number_rule_1
import time


def get_guess():
    """
    Gets the input from the user.

    :return: the user's input, an integer
    """
    while True:
        try:
            n = int(input('Enter your guess: '))
            break
        except ValueError:
            print('That\'s not an integer!')
    return n


def check_for_code_runners(secret_num, guess):
    """
    Prints the number of codes and runners, being given the secret number and the guess.

    :param secret_num: the secret number
    :param guess: the user's current guess
    :return: prints the number of codes and runners
    """
    secret = []
    g = []
    code = 0
    runners = 0
    while secret_num > 0:
        secret.append(secret_num % 10)
        secret_num = secret_num // 10
    while guess > 0:
        g.append(guess % 10)
        guess = guess // 10
    for index in range(4):
        if g[index] == secret[index]:
            code += 1
        elif g[index] in secret:
            runners += 1
    print(f'There are {code} codes and {runners} runners!')


def run_console():
    secret_num = generate_random_secret_number()
    start_time = time.time()
    while True:
        now = time.time()
        if now - start_time >= 60:
            print('Game over! No time left!')
            break
        guess = get_guess()
        now = time.time()
        if now - start_time >= 60:
            print('Game over! No time left!')
            break
        if guess == 8086:
            print(f'The secret number is {secret_num}!')
        elif not check_number_rule_1(guess):
            print('You\'ve lost the game! That\'s not a valid guess!')
            break
        elif guess == secret_num:
            print('You\'ve won the game! That was the secret number!')
            break
        else:
            check_for_code_runners(secret_num, guess)
        now = time.time()
        if now - start_time >= 60:
            print('Game over! No time left!')
            break
