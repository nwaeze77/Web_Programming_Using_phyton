# This asked student to input their grades in other to determine their status

grade = float(input('Whats is your grade: '))
name = input('Whats your name: ')
A = 'grade >= 90'
B = 'grade >= 80'
C = 'grade >= 70'
D = 'grade >= 60'
F = 'grade < 60'

#letter = {'A':'grade >= 90','B':'grade >= 80','C':'grade >= 70','D':'grade >= 60','F':'grade < 60'}

letter = A, B, C, D, F

sign = '+', '-', ''

# This if statement determines the student grade

if grade >= 90:
     letter = 'A'
     sign = ''
     if grade % 10 < 3:
          sign = '-'

elif grade >= 80:
     letter = 'B'
     sign = '' 
     if grade % 10 >= 7:
          sign = '+'
     if grade % 10 < 3:
          sign = '-'

elif grade >= 70:
     letter = 'C'
     sign = ''
     if grade % 10 >= 7:
          sign = '+'
     if grade % 10 < 3:
          sign = '-'
        
elif grade >= 60:
     letter = 'D'
     sign = ''
     if grade % 10 >= 7:
          sign = '+'
     if grade % 10 < 3:
          sign = '-'
        
else:
     grade < 60
     letter = 'F' 
print(f'{name}, you got {letter}{sign} in this course')  



      
