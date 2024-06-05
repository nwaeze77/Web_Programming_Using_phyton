# I added 'verb_1', 'verb_2', 'name' and 'faculty' to the original story.
# 'verb_1' and 'verb_2' were added so as to avoid verb repetition, 'name' represents the name of my little sister and 'faculty' represents the name of the department we were in.

adjective = input('input an adjective: ')
animal = input('input name of an animal: ')
verb = input('input a verb: ')
exclamation = input('input an exclamation: ')
verb_1 = input('input another verb: ')
verb_2 = input('input yet another verb: ')
name = input('input a girls name: ')
faculty = input('input a school department name: ')

output = f' The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb} down the hallway. "{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb_1} over and over. Miraculously, that caused it to stop, but not before it tried to {verb_2} right in front of my family, causing my little sister {name} to pee on herself. Some students of {faculty} department who saw what had happened sympathized with us.'

print(output)