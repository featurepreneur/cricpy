'''
Created on 
    Feb 19, 2022 - Sunday 

Course work: 
    Python for Cricket Lovers

@author: Raja CSP

Source:
    https://github.com/tactlabs/tact-python/tree/master/csp/cricket
'''

# Import necessary modules
import random 

# Constants
BALLS_PER_OVER = 6

def get_random_number(min = 0, max = 6):

    return random.randint(min, max)

def get_random_score():

    return get_random_number(0, 6)

def play_single_over():

    current_over = BALLS_PER_OVER

    total_score_c_over = 0

    for _ball in range(current_over):

        _ball += 1

        c_run = get_random_score()

        total_score_c_over += c_run

        print(f'ball: {_ball}, run: {c_run}, total_score_current_over: {total_score_c_over} ')

def startpy():

    # r_score = get_random_score()
    # print(r_score)

    play_single_over()

    pass

if __name__ == '__main__':
    startpy()