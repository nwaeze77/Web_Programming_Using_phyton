# I added the While loop to ensure that only a string is inputed in the variable name.

print(f'Welcome to "OKIJA FOREST"')

# I used the "isalpha" function to ensure that the name input is alphbet
name = str(input('Whats is your name: ')) 

while True:

    if name.isalpha():
        print(f'{name} before you step into OKIJA FOREST you will find Three weapons a "GUN, KNIEF and MAP Which one do you want to pick up?')
        break
    
    else:
        print(f'Wrong input, input must be a string(letter)')
        name = str(input('Whats is your name: '))
        

# I want to suggest available weapons for the player to pick from

weapon = str(input(f'chose your weapon: GUN, KNIEF or MAP '))
WeaponChoice = bool(True)
if WeaponChoice == True:
    MakeYourChoice = str(input(f'Do you want to PROCEED OR CHANGE_WEAPON: '))

    if MakeYourChoice == 'PROCEED'.lower():
        print(f'Get READY {name.lower()}')

    else:
        print(f'Choose another weapon')
        weapon = str(input('chose your weapon: GUN, KNIEF or MAP: '))
        MakeYourChoice = str(input(f'Do you want to PROCEED OR CHANGE_WEAPON: '))
       

# Senario 1 if a gun is picked as weapon

    if weapon == 'GUN'.lower():
        print(f'You picked a {weapon.lower()} great CHOICE! you have just three shots and if you shot, other animlas will be alerted: OH! NO! you are out of bullets and you are attacked by a Tiger what would you want to RUN, STAND or SCREAM?')            
        next = str(input('What would you do  RUN, STAND or SCREAM: ')).lower()
    

        if next == 'RUN'.lower():
            print(f'Be careful because there could be booby trap anywhere') 

        elif next == 'STAND'.lower():
            print(f'You are courageous, but you are on your own')

        elif next == 'SCREAM'.lower():
            print(f'Help is coming your way {name.lower()} hold on!')    
    
        else:
            print(f'Wrong input! try again')
          

# Senario 2 if Knief is picked as a weapon

    if weapon == 'KNIEF'.lower():
        print(f'You picked a {weapon.lower()} great CHOICE! You will have to navigate your way through the forest.You have two option "KEEP A LOW PROFILE" or "RISK IT ALL"  ?')
        next = str(input('What would you do  "KEEP A LOW PROFILE" or "RISK IT ALL": ')).lower()
    

        if next ==  'KEEP A LOW PROFILE'.lower():
            print(f'SMART!! you can careful seek/crwal and encounter less dangerous animals along the way.') 

        elif next == 'RISK IT ALL'.lower():
            print(f'FEISTY!! You must be a pro')  

        else:
            print(f'Wrong input! try again')    


# Senario 3 if a Map is picked as a weapon
    if weapon == 'MAP'.lower():
        print(f'You picked a {weapon.lower()} great CHOICE! Now you have the EYES of the forest you can easily navigate your way around safely. Would you "USE IT" or "PUT IT AWAY"?')
        next = str(input('What would you do  "USE IT" or PUT IT AWAY: ')).lower()
    

        if next ==  'USE IT'.lower():
            print(f'GENIUS! See you at the other side') 


        elif next == 'PUT IT AWAY'.lower():
            print(f'OOPS! Hope yo know what you are doing')  

        else:
            print(f'Wrong input! try again')            