#checks user entered yes (y) or no (n)

def yes_no (question):
                
                while True:
                                response = input (question).lower()
                                #checks user response, question
                                #repeats if users don't enter yes/no
                        
                                if response == 'yes' or response == 'y':
                                                return 'yes'
                                elif response == 'no' or response == 'n':
                                                return 'no'
                                else:
                                                print ('You did not enter a valid response. Please enter yes or no.')                                  
                
                                 
    
#displays instructions to user
def instructions():
                print ('''
                
***** Instructions ******

To begin, decide on a score goal (eg: The first one to get a score of 50 wins).

For each round of the game, you win points by rolling dice. 
The winner of the round is the one who gets 13 (or slighly less).

If you win the round, your score will increase by the number of points that you earned. 
If your first roll of two dice is a double (eg: both dice show a three), then your
score will be DOUBLE the number of points. 

If you lose the round, the you don't get any points. 

If you and the computer tie, (eg: you both get a score of 11) you will have 11 points 
added to your score. 

Your goal is to try to get to the target score before the computer.

Good luck.

                
                
                
                ''')  

#checks that users enter an integer
#that is more than 13

def int_check():
                while True:
        
                                error = 'Please enter an integer that is 13 or more'
                                try:
                                                response = int(input('Enter an integer: '))
                                           
                                    #checks that the number is more than / equal to 13
                                                if response < 13:
                                                                print (error)
                                                else: 
                                                                return response
                                except ValueError:
                                                print (error)
                        

# Main Rountine

print ()
print ('🎲🎲 Roll it 13 🎲🎲')
print ()
#loop for testing purposes

want_instructions = yes_no('Do you want to read the instructions? ')

#checks user enters yes (y) or no (n)

if want_instructions == 'yes':
                instructions()

print ()

target_score = int_check()
          


'''
while True:
                
        want_instructions = yes_no (' Do you want to read the instructions? ')
        print (f' You chose {want_instructions}')
        



                while response != 'yes' and response != 'no' and response != 'n' and response != 'y':
                        print ('You did not choose a valid response. Try again. ')
                        response = input (' Do you want to read the instructions? ').lower()
'''