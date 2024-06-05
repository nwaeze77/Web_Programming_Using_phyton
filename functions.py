import math

# Compute and return areas of Square, Rectangle and Circle

def compute_area_square(side):
    area_square = side * side
    return area_square


def compute_area_rectangle(lenght, breath):
    area_rectangle = lenght * breath
    return area_rectangle


def compute_area_circle(radius):
    area_circle = 2 * 3.142 * radius * radius
    return area_circle


# A loop to determine the kind of shape until quit is chosen

options = ['Square', 'Rectangle', 'Circle', 'Quit']

print(f'Pick the kind of shape to determine the Area: ')

while True:

    for i, kind in enumerate(options, start = 1):
    
        print(f' {i}.  {kind}')

    kind = input('Chose a shape to proceed or Quit to exit: ').capitalize()

    try:
        kind = int(kind)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if 1 <= kind <= len(options):
        selected_option = options[kind - 1]
        print(f"You selected: {selected_option}")

    if selected_option == 'Square':
        side = int(input('Input value of side of the square in meters: '))
        square_area = compute_area_square(side)
        print(f' The area of the square is: {square_area:.2f}m')

    # if selected_option == 'Square':
    #     square_area = compute_area_rectangle(side)
    #     print(f' The area of the square is: {square_area:.2f}m')


    elif selected_option == 'Rectangle':
        lenght = int(input('Input value of lenght of rectangle in meters: '))
        breath = int(input('Input value of breath of rectangle in meters: '))
        rectangle_area = compute_area_rectangle(lenght, breath)
        print(f' The area of the rectangle is: {rectangle_area:.2f}m')    

    elif selected_option == 'Circle':
        radius = int(input('Input value of radius of circle in meters: '))
        circle_area = compute_area_circle(radius)
        print(f' The area of the circle is: {circle_area:.2f}m')

    elif selected_option == 'Quit':
        print('Goodbye')
        break    




