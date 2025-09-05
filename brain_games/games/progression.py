import secrets

from brain_games.games.engine import run_game

from .consts import (
    MAX_PROGR_LENGHT,
    MIN_PROGR_LENGHT,
    PROGRESSION_INSTRUCTION,
)


def secure_randint(min_val, max_val):
    return secrets.randbelow(max_val - min_val + 1) + min_val


def progr():
    start, step = secrets.randbelow(100) + 1, secrets.randbelow(100) + 1
    progr = []
    progr_lenght = secure_randint(MIN_PROGR_LENGHT, MAX_PROGR_LENGHT)

    for i in range(progr_lenght):
        progr.append(start + step * i)

    missed_index = secrets.randbelow(progr_lenght - 1) + 1
    missed_num = progr[missed_index]
    progr[missed_index] = '..'
    progr_with_missed_num = ' '.join(map(str, progr))

    return progr_with_missed_num, str(missed_num)


def run_progression_game():
    run_game(progr, PROGRESSION_INSTRUCTION)



