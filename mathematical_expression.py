# A program to convert from Fahrenheit to Celsius
fahrenheit = int(input('What is the tempreture in Fahrenheit?: '))
celsius = (fahrenheit - 32) * 5/9
output = f'The tempreture in Celsius is {celsius:.1f} degrees.'
print(output)

