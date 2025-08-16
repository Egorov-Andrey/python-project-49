from random import randint

import prompt


def main():

    number_question = randint(1, 100)

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')

    print('Hello, ' + name + '!')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    num_correct_input = 0
    num_of_times = 2
    number_question = randint(1, 100)
    print('Question: ' + str(number_question))
    answer_user = prompt.string('Your answer: ')
    if answer_user == even_or_otherwise(number_question):
        print('Correct!')

    while num_correct_input < num_of_times:

        if answer_user == even_or_otherwise(number_question):
            number_question = randint(1, 100)
            print('Question: ' + str(number_question))
            answer_user = prompt.string('Your answer: ')
            print('Correct!')
            num_correct_input += 1
            if num_correct_input == 3:
                print('Congratulations, ' + name + '!')
        elif answer_user != even_or_otherwise(number_question):
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name + '!')
            break
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name + '!')
            break
          
    print('Congratulations, ' + name + '!')


def even_or_otherwise(number_question):
    if number_question % 2 == 0:
        return 'yes'
    return 'no'
