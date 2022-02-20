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
import time

# Local import

# Constants
TOTAL_OVERS     = 3
BALLS_PER_OVER  = 6
CURRENT_TEAMS   = [
    'India',
    'Australia'
]
QUICK_TESTING   = False

# Other variables
team_a_total_score = 0
team_b_total_score = 0

def get_random_number(min = 0, max = 6):

    return random.randint(min, max)

def get_random_score():

    return get_random_number(0, 6)

def ball_gap():

    if(QUICK_TESTING):
        return

    time.sleep(1)

def pgap(count = 1):

    for _count in range(count):
        print('')

def play_single_over(chase_flag = False):

    current_over = BALLS_PER_OVER

    total_score_c_over = 0

    for _ball in range(current_over):

        ball_gap()

        _ball += 1

        c_run = get_random_score()

        total_score_c_over += c_run

        # if(c_run == 4):
        #     print(f"It's a fantastic Four!!")

        print(f'[ball {_ball}]: run: {c_run}')

        # print(f'ball: {_ball}, run: {c_run}, total_score_current_over: {total_score_c_over} ')

    pgap()
    print(f'total_score_current_over : {total_score_c_over}')

    return total_score_c_over

def print_score_board(
    current_over,
    team_innings_score
):

    print(f'Scoreboard: {team_innings_score}/0 [{current_over} overs]')

def play_inninings(
    chase_flag = False, 
    over_count = 1,
    chasing_score = 0
):

    team_innings_score = 0
    for _c_over in range(over_count):

        current_over = _c_over + 1

        print(f'playing : over {current_over}')
        print('-' * 17)

        team_innings_score += play_single_over()

        pgap()

        print_score_board(
            current_over,
            team_innings_score
        )

        # print(f"trap1763 : team_innings_score: {team_innings_score}, chasing_score: {chasing_score}")

        if(chase_flag):
            if(team_innings_score > chasing_score):
                # print(f'Beat the score: chasing_score: {chasing_score}, team_innings_score : {team_innings_score}')
                return team_innings_score

        pgap()


    return team_innings_score

def play_team_a(team_a):

    # First team batting
    print(f'{team_a} batting: ')
    pgap()
    team_a_total_score =  play_inninings(
        over_count = TOTAL_OVERS
    )
    pgap()
    print(f'{team_a} scored: {team_a_total_score}')

    print('-' * 77)

    return team_a_total_score

def play_team_b(
    team_b,
    chasing_score
):

    # print(f"team_a_total_score : {team_a_total_score}")

    pgap()
    print(f'{team_b} batting: ')
    pgap()
    team_b_total_score =  play_inninings(
        chase_flag = True, 
        chasing_score = chasing_score,
        over_count = TOTAL_OVERS
    )
    pgap()
    print(f'{team_b} scored: {team_b_total_score}')

    return team_b_total_score

def choose_winner(
    team_a,
    team_b,

    team_a_total_score,
    team_b_total_score
):
    
    if(team_b_total_score > team_a_total_score):
        print(f'{team_b} won')
        return 

    if(team_b_total_score == team_a_total_score):
        print(f"What a match! It's a draw!!")
        return 

    print(f'{team_a} won') 

def play_game():

    team_a = CURRENT_TEAMS[0]
    team_b = CURRENT_TEAMS[1]

    # First team batting
    team_a_total_score = play_team_a(team_a)

    # print(f'team_a_total_score: {team_a_total_score} ')
    
    # Second team batting
    team_b_total_score = play_team_b(
        team_b,
        team_a_total_score
    )
    
    # Choose winner
    choose_winner(
        team_a,
        team_b,

        team_a_total_score,
        team_b_total_score
    )

    # 
    pass

def startpy():

    play_game()

if __name__ == '__main__':
    startpy()