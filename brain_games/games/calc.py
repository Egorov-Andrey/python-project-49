import secrets

from .consts import CALC_INSTRUCTION, MATH_SIGNS
from .engine import run_game


def get_result_by_math_sign(number_1, number_2, math_sign):

    match math_sign:
        case '+':
            return number_1 + number_2
        case '-':
            return number_1 - number_2
        case '*':
            return number_1 * number_2
        case _:
            raise ValueError(f'Unsoported operator: {math_sign}')


def get_math_expression_and_result():

    number_1, number_2 = secrets.randbelow(100) + 1, secrets.randbelow(100) + 1

    math_sign = secrets.choice(MATH_SIGNS)

    result = get_result_by_math_sign(number_1, number_2, math_sign)

    exception = f"{number_1} {math_sign} {number_2}"

    return exception, str(result)


def run_calc_game():
    run_game(get_math_expression_and_result, CALC_INSTRUCTION)