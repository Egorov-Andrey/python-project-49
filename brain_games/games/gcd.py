import random

from brain_games.consts import GCD_INSTUCTION
from brain_games.engine import run_game


def get_two_num_and_gcd_answer():

    num_1, num_2 = random.randint(1, 100), random.randint(1, 100)
    pair = f'{num_1} {num_2}'

    while num_2 != 0:
        remainder = num_1 % num_2
        num_1 = num_2
        num_2 = remainder
    
    gcd = num_1

    return pair, str(gcd)


def run_gcd_game():
    run_game(get_two_num_and_gcd_answer, GCD_INSTUCTION)