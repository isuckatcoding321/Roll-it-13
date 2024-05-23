print ()

import random

#generates an integer between 0 and 6
#to simulate the roll of a die

def roll_die():
    result = random.randint(1,6)
    return result

#rolls two dice and returns total and whether we
#had a double roll

def two_rolls():
    
    double_score = 'no' 
    
    #roll two dice
    roll_1  = roll_die()
    roll_2  = roll_die()
    
    #check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = 'yes'
        
    user_points = roll_1 + roll_2
    
    #show the user the result
    print (f'Die 1: {roll_1} \t Die_2: {roll_2} ')
    
    return user_points, double_score   

#main routine starts here
'''
die_roll = roll_die()
print (die_roll)
'''

how_many = int(input ('How many dice?: '))
               
               
for item in range (0,5):

    if how_many == 2:
    
        start_points = two_rolls()
        points = start_points [0]
        double_points = start_points [1]
        
        print (f'You have {points} points and a double score of {double_points}')
   
   
   
   
   
'''
user_score= 0
double_score = 'no'
    
'''