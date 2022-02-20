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
TOTAL_OVERS     = 2
BALLS_PER_OVER  = 6
TOTAL_WICKETS   = 10
CURRENT_TEAMS   = [
    'India',
    'Australia'
]
QUICK_TESTING   = False

# Other variables
# team_a_total_score = 0
# team_b_total_score = 0

def get_random_number(min = 0, max = 6):

    return random.randint(min, max)

def is_wicket():

    r_number = get_random_number()

    if(r_number % 7 == 0):
        return True

    if(r_number % 9 == 0):
        return True

    return False

def get_random_score():

    r_score = get_random_number(0, 6)

    if(r_score == 5):
        return 4

    return r_score

def ball_gap():

    if(QUICK_TESTING):
        return

    time.sleep(1)

def pgap(count = 1):

    for _count in range(count):
        print('')

def play_single_over(
    chase_flag          = False,
    chasing_score       = 0,
    team_current_score  = 0
):

    current_over = BALLS_PER_OVER

    total_score_c_over = 0

    for _ball in range(current_over):

        ball_gap()

        _ball += 1

        # Check wicket
        wicket_flag = is_wicket()

        if(wicket_flag):
            c_run = 0

            print(f"[ball {_ball}]: It's a wicket ")
        else:
            c_run = get_random_score()
            total_score_c_over += c_run

            team_current_score += c_run

            # print(f'[ball {_ball}]: run: {c_run}')

            # Enable only for testing purpose
            print(f'[ball {_ball}]: run: {c_run}, total_score_current_over: {total_score_c_over}, team_current_score : {team_current_score} ')

        if(chase_flag):
            if(team_current_score > chasing_score):
                print(f'Beat the score: chasing_score: {chasing_score}, team_innings_score : {team_current_score}')
                return team_current_score

        # if(c_run == 4):
        #     print(f"It's a fantastic Four!!")

        # print(f'ball: {_ball}, run: {c_run}, total_score_current_over: {total_score_c_over} ')

    pgap()
    print(f'total_score_current_over : {total_score_c_over}')

    return team_current_score

def print_score_board(
    current_over,
    team_innings_score
):

    print(f'Scoreboard: {team_innings_score}/0 [{current_over} overs]')

def play_inninings(
    chase_flag = False, 
    over_count = 1,
    chasing_score = 0,
    # team_current_score = 0
):

    team_innings_score = 0
    for _c_over in range(over_count):

        current_over = _c_over + 1

        print(f'playing : over {current_over}')
        print('-' * 17)

        team_innings_score = play_single_over(
            chase_flag          = chase_flag, 
            chasing_score       = chasing_score,
            team_current_score  = team_innings_score
        )

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

        chase_flag          = False, 
        over_count          = TOTAL_OVERS,
        chasing_score       = 0,
        # team_current_score   = 0
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
        chase_flag          = True, 
        chasing_score       = chasing_score,
        over_count          = TOTAL_OVERS,
        # team_current_score   = 0
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
    team_a_total_score = play_team_a(
        team_a
    )

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


'''
    Issues:

    - Runs 5 should be removed : DONE
    - 

'''