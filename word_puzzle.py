# WELCOME TO WORD GUESSING GAME

# I added a limitation to number of guesses pegging at 5

# This first part is where i store my variable aside "Feedback"
name = str(input('What is your name: '))

secret = 'computer'

secret_len = ' _ ' *  len(secret)

guess = str(input('Whats is your guess: '))

guess_len = ' _ ' * len(guess)

NoOfGuesses = 0

print(f'Your Hint is {secret_len}')

# This loop ensures that the same number of letters as the secret word is entered
# It then shows Hint.
while True:
    feedback = ''
    
    if guess_len != secret_len:
        print('Sorry, the guess must have the same number of letters as the secret word.')
        guess = str(input('Whats is your guess: '))
        guess_len = ' _ ' * len(guess)
        NoOfGuesses += 1

        if NoOfGuesses == 5:
            print(f'You have reached the maximum number of guesses which is {NoOfGuesses}')
            if guess.lower() == secret:
                print(f'However Congratulations! {name} You guessed it!')
            break
            
    elif guess_len == secret_len:
        for secret_letter, guess_letter in zip(secret, guess.lower()):
        
            if secret_letter == guess_letter:
                feedback += secret_letter.upper()
            elif guess_letter in secret:
                feedback += guess_letter.lower()
            elif guess_letter not in secret: 
                feedback += ' _ '
        print(f'Your hint is: {feedback}')
        NoOfGuesses += 1
        

        if guess.lower() == secret:
            print(f'Congratulations! {name} You guessed it!')
            break
        
        guess = str(input('Whats is your guess: '))       

        if NoOfGuesses == 5:
                print(f'You have reached the maximum number of guesses which is {NoOfGuesses}')
                if guess.lower() == secret:
                    print(f'However Congratulations! {name} You guessed it!')
                break
                    
            
    
print(f'You used {NoOfGuesses} guesses.')


        

