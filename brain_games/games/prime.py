import random

from brain_games.consts import PRIME_INSTUCTION
from brain_games.engine import run_game


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return False
    return True


def get_num_and_prime_ans():
    number_question = random.randint(1, 100)

    result = 'yes' if is_prime(number_question) else 'no'

    return number_question, result


def run_game_prime():
    run_game(get_num_and_prime_ans, PRIME_INSTUCTION)
