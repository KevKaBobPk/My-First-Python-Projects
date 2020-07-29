#id: babuake1
#lang: python 3
#task: ride

converter = {'a': 1, 'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26,}

top_string = str(input())
bottom_string = str(input())
product1 = 1
mod1 = 0
product2 = 1
mod2 = 0

for letter in top_string:
    product1 = product1 * (converter[letter.lower()])


for letter in bottom_string:
    product2 = product2 * (converter[letter.lower()])
    

mod1 = product1 % 47
mod2 = product2 % 47

if mod1 == mod2:
    print("GO")
else:
    print("STAY")
    