import prompt

from .consts import AMOUNT_OF_ROUND


def run_game(get_question_and_answer, instruction):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!\n'
        f'{instruction}')

    for _ in range(AMOUNT_OF_ROUND):
        question, answer = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\n'
                                    f'Your answer: ')
        
        if user_answer == answer:
            print('Correct!')
        else: 
            print(f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer is '{answer}'.\n"
                f"Let's try again, {name}!")
            
            return 

    print(f"Congratulations, {name}!") 

