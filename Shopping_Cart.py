# Welcome to the Shopping Cart Program!

# I included mode of payment to the menu, with just limited functionality for now.

menu = ['Add item', 'View cart', 'Remove item', 'Compute total', 'Payment Method', 'Quit']

mode_of_payment = ['Paypal', 'Credit Card', 'Debit Card', 'Cash']

shopping_cart = []

prices = []

while True:

    print('Please select one of the following:')
    for i, item in enumerate(menu, start = 1):
        print(f'{i}. {item}')

    action = str(input('Please enter an action: '))

    try:
        action = int(action)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if 1 <= action <= len(menu):
        selected_option = menu[action - 1]
        print(f"You selected: {selected_option}")

        if selected_option == 'Add item':
            add = str(input('What item would you like to add?  '))
            amount = float(input(f'What is the price of {add}?  '))
            print(f'You added {add} to the shopping_cart! ')
            shopping_cart.append(add)
            prices.append(amount)
            print(shopping_cart, prices)

        elif selected_option == 'View cart':
            print('The contents of the shopping cart are:')
            for j, (goods, cost) in enumerate(zip(shopping_cart, prices), start = 1):
                print(f'{j}. {goods} - ${cost:.2f} ')

        elif selected_option == 'Remove item':
            delete = int(input('What is the index of what you want to remove: ')) - 1
            if 0 <= delete <= len(shopping_cart):
                shopping_cart.pop(delete)
                prices.pop(delete)
                print('Item removed.')
                print(shopping_cart, prices)

        
        elif selected_option == 'Compute total':
            total = sum(prices)
            print(f'The total price of the items in the shopping cart is ${total:.2f}')

        elif selected_option == 'Payment Method':
            for k, method in enumerate(mode_of_payment, start = 1):
                print(f' {k}   {method}')
            mode = int(input('Which payment method do you prefer: '))
            
            if 1 <= mode <= len(mode_of_payment):
                mode = mode_of_payment[mode - 1]
                print(f"You selected: {mode}")  
                
                if mode == 'Cash':
                    total = sum(prices)
                    print('You can proceed to the counter!')
                    print(f'You are to pay ${total:.2f}')

                else:
                    card_name = []
                    card_number = []
                    cvv = []
                    print('Input card Details: ') 
                    card_name = str(input('Please input name on card: '))
                    card_number = int(input('PLease input card number: '))
                    cvv = int(input('Please input your cvs: '))
                    print('Please confirm that your information is correct')
                    print(f' Name: {card_name}, Number: {card_number}, CVV No.: {cvv}')
                    break



        if selected_option == 'Quit':
            print("Exiting the program.")
            break

print('Thank You!  Goodbye!')    