# Snake, Water and gun game

import random     # built in module 

computer = random.choice([1,0,-1])
you = input("Enter choices from Snake ,Gun and Water: ").lower()
dict = {"snake": 1 , "gun": 0 , "water": -1 }
reversedict = {1 :"snake" , 0 :"gun" , -1 :"water"}   # for printing what computer chooses
youstr = dict[you]

print(f"You chooses: {you}\ncomputer chooses: {reversedict[computer]}")

if (computer == youstr ):
    print("It's a draw!")
else:
    ''' 
    # shorten way of this condition part is:
    if ((computer - youstr) == 1 and (computer - youstr) == -2):
       print("you win!)
    else:
       print("you loose!)     
    '''
    if (computer == 1 and youstr == 0):      # (computer - youstr) = 1 ->win
        print("You win!")
    elif (computer == 1 and youstr == -1):   # (computer - youstr) = 2 ->loose
        print("You loose!")    
    elif (computer == 0 and youstr == -1):   # (computer - youstr) = 1 ->win
        print("You win!")    
    elif (computer == 0 and youstr == 1):    # (computer - youstr) = -1 ->loose
        print("You loose!")    
    elif (computer == -1 and youstr == 1):   # (computer - youstr) = -2 ->win
        print("You win!")    
    elif (computer == -1 and youstr == 0):   # (computer - youstr) = -1 ->loose
        print("You loose!")    
    else:
        print("Something went wrong!")   
        