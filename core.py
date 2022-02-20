'''
Created on 
Course work: 
@author: raja
Source:
    
'''

# Import necessary modules
import random 

def get_random_number(min = 0, max = 6):

    return random.randint(min, max)

def get_random_score():

    return get_random_number(0, 6)

def startpy():
    
    # print("Whatsup Toronto")

    r_score = get_random_score()
    print(r_score)


if __name__ == '__main__':
    startpy()