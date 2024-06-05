# I will be adding drink to the original program, hence i will be making calculations for both meal and drink.
# This program is to compute the price of meal and drink

child_meal = float(input('The price of a child meal: '))
child_drink = float(input('The price of a child drink: '))

adult_meal = float(input('The price of an adult meal: '))
adult_drink = float(input('The price of an adult drink: '))

number_of_children = int(input('The number of children: '))

number_of_adult = int(input('The number of adults: '))

# This program calculates the subtotals

child_subtotal_meal = child_meal * number_of_children
child_subtotal_drink = child_drink * number_of_children

adult_subtotal_meal = adult_meal * number_of_adult
adult_subtotal_drink = adult_drink * number_of_adult

subtotal_meal = child_subtotal_meal + adult_subtotal_meal
subtotal_drink = child_subtotal_drink + adult_subtotal_drink


print(f'Subtotal_meal is: ${subtotal_meal:.2f}')
print(f'Subtotal_drink is: ${subtotal_drink:.2f}')

# This program collects the sales tax rate and determines the sales tax 

sales_tax_rate = float(input('What is the sales tax rate? eg 6 or 6.5 not 0.006 or 0.065: '))

sales_tax_meal = (subtotal_meal * sales_tax_rate) / 100
sales_tax_drink = (subtotal_drink * sales_tax_rate) / 100

print(f'Sales tax for meal is: ${sales_tax_meal:.2f}')
print(f'Sales tax for drink is: ${sales_tax_drink:.2f}')

# Computing the total price of the meal

total_price_meal = subtotal_meal + sales_tax_meal
total_price_drink = subtotal_drink + sales_tax_drink

print(f'Total price for meal is: ${total_price_meal:.2f}')
print(f'Total price for drink is: ${total_price_drink:.2f}')

# Calculate change given payment amount

payment_amount = float(input('What is the payment amount for meal?: '))
payment_amount = float(input('What is the payment amount for drink?: '))

change_meal = payment_amount - total_price_meal
change_drink = payment_amount - total_price_drink

print(f'Change for the meal is: ${change_meal:.2f}')
print(f'Change for the drink is: ${change_drink:.2f}')

