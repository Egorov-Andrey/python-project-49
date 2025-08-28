import random

from brain_games.consts import EVEN_INSTUCTION
from brain_games.engine import run_game


def is_even(number_question):

    return number_question % 2 == 0


def get_num_and_even_ans() -> tuple:

    number_question = random.randint(1, 100)

    result = 'yes' if is_even(number_question) else 'no'
    
    return number_question, result


def run_even_game():
    run_game(get_num_and_even_ans, EVEN_INSTUCTION)

