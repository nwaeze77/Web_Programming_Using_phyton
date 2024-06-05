
secret = 'computer'

guess = str(input('Whats is your guess: '))

NoOfGuess = 0 

while True:
        
    if guess != secret:
        print('Sorry, your guess was not correct.')
        guess = str(input('Whats is your guess: '))
        NoOfGuess += 1

    else:
        print('Congratulations! You guessed it!')
        NoOfGuess += 1
        break
print(f'it took you {NoOfGuess} guesses ')    