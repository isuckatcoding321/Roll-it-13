print ('🎲🎲 Roll it 13 🎲🎲')

# checks user enters yes (y) or no (n)

def yes_no (question):
    
        while True:
        
                response = input (question).lower()
                
                while response != 'yes' and response != 'no' and response != 'n' and response != 'y':
                        print ('You did not choose a valid response. Try again. ')
                        response = input (' Do you want to read the instructions? ').lower()
                
                if response == 'yes' or response == 'y':
                        return 'yes'
                elif response == 'no' or response == 'n':
                        return 'no'
    

# Main Rountine

while True:
                
        want_instructions = yes_no (' Do you want to read the instructions? ')
        print (f' You chose {want_instructions}')
        
