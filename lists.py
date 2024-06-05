name = input('Whats your favourite : ')

items = []

while name != 'quit':
        items.append(name)
        name = input('Whats your favourite : ')


        if name == 'quit':
                break
        

print(items)  

for item in items:
        print(item)
for index in range(len(items)):
        item = items[index]
        print(f'{index} is {item}')
index = int(input('input a number in square bracket e.g[]  :' ))
new_favourite = str(input('input new favourite: ')) 
items[index] = new_favourite
for i in items:
        print(i)
        print(items)


           