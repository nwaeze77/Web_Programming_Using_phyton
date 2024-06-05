# Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.
age = input('How old are you: ')
next_birthday = int(age) + 1
output = f'On your next birthday, you will be {next_birthday}'
print(output)

# Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.
egg_cartoon = input('How many egg cartoon do you have?: ')
egg_cartoon_by_12 = int(egg_cartoon) * 12
output = f'You have {egg_cartoon_by_12} eggs.'
print(output)

# Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.
cookies = input('How many cookies do you have?: ')
people = input('How many person do you have?: ')
cookies_per_people = int(cookies) / int(people)
output = f'Each person may have {cookies_per_people} cookies'
print(output)
