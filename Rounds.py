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


#Main routine starts here

print ('Please <enter> to begin this round: ')
input ()

#get initial dice rolls for user
user_first = two_rolls()
user_points = user_first [0]
double_points = user_first [1]

#Tell the user if they are eligible for double points
if double_points == 'no':
    double_feedback = ''
else:
    double_feedback = 'If you win this round, you gain double points!'
    
#output initial move results 
print (f'You rolled a total of {user_points}. {double_feedback}')
print ()   

#get initial dice rolls for computer
computer_first = two_rolls()
computer_points = computer_first [0]

print (f'The computer rolled a total of {computer_points}')


#Loop (while both user / computer have <= 13 points)...
while user_points < 13 and computer_points < 13:
    
    # ask user if they want to roll again, update
    #points / status
    print ()
    roll_again = input ("Do you want to roll the dice again? (type 'no' to pass): ")
    if roll_again == 'yes':
        user_move = roll_die()
        user_points += user_move
        print (f'You rolled a {user_move}. You now have {user_points}.')
        
        #If user points goes over 13, tell them that they lose and set points to 0.
        
        if user_points > 13:
            print (f'Oops! You rolled a {user_move} so your total is {user_points}.'
                   f'Which is over 13 points so you lose this round and'
                   f"don't get any points added to your total score.")
    
            #reset user points to 0 so that when we update their
            #score at the end of the round it is correct. 
            user_points = 0 
            
            break 
        
        else:
            print (f'You rolled a {user_move} and have a total score of {user_points}.')
    

    
# roll die for computer and update computer points 
    computer_move = roll_die()
    computer_points += computer_move
    print (f'The computer has rolled a {computer_move}. The computer '
           f' now has {computer_points}.')
           
    print ()
    if user_points > computer_points:
        result = 'You are ahead'
    else:
        result = 'The computer is ahead'
        
    
    print (f'****Round update****: {result}')
    print (f'User score: {user_points} \t | \t Computer score: {computer_points}')
    

'''
again_q = input ('Do you want to roll again? y or n? ').lower()
    if again_q == 'y':
        roll_2 = two_rolls()
        user_points = user_points + roll_2

if roll_1 == roll_2:
    print (double_score)

print (f'You got {user_points} and the computer got {computer_points}!')

if user_points > computer_points:
    print ('You won!')

else:
    print ('You lost :(')
'''

#Outside loop - double user points if they won and are eligible

#show rounds result

if user_points < computer_points:
    print ("Sorry you have lost this round and no points"
           "have been added to your total score. The computer's score has"
           f"increased by {computer_points} points.")
    
#currently does not include double points!

else:
    print (f"Yay! You won the round and {user_points} points have"
           f" been added to your score")