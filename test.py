import numpy as np



number_of_tries = 0

magic_number = np.random.randint(1,20)
guess_number = int(input('Guess a number '))

while True:

   if guess_number > magic_number:
      print('Lower')
      guess_number = int(input('Guess a number '))
      number_of_tries = number_of_tries + 1
      

   elif guess_number < magic_number:
      print('Higher')
      guess_number = int(input('Guess a number '))
      number_of_tries = number_of_tries + 1

   else:
      print('You guessed it!')   
      break

print(f'You guessed it right in {number_of_tries} tries')