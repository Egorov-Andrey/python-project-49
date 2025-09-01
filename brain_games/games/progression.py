import random

from brain_games.consts import (
    MAX_PROGR_LENGHT,
    MIN_PROGR_LENGHT,
    PROGRSSION_INSTUCTION,
)
from brain_games.engine import run_game


def progr():
    start, step = random.randint(1, 100), random.randint(1, 100)
    progr = []
    progr_lenght = random.randint(MIN_PROGR_LENGHT, MAX_PROGR_LENGHT)

    for i in range(progr_lenght):
        progr.append(start + step * i)

    missed_index = random.randint(0, progr_lenght)
    missed_num = progr[missed_index]
    progr[missed_index] = '..'
    progr_with_missed_num = ' '.join(map(str, progr))

    return progr_with_missed_num, str(missed_num)


def run_progression_game():
    run_game(progr, PROGRSSION_INSTUCTION)



