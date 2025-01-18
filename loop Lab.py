#Exercise 1

for i in range (-5,6):
    print (i)

#Exercise 2

Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i, Genres in enumerate (Genres):
    print (i,Genres)    

#Exercise 3

squares=['red', 'yellow', 'green', 'purple', 'blue']
for squares in squares:
    print (squares)

#Exercise 4

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while (i<len(squares) and squares [i] == 'orange'):
    new_squares = (squares [i])
    i = i+1
    print (new_squares)

#Real Life 1

print ("Tables of 6:")
for i in range (10):
    print ("6*",i,"=",6*i)
print ("Tables of 7:")
for i in range (10):
    print ("7*",i,"=",7*i)

#Real Life 2
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
seven = []
i = 0
while i<len(Animals):
    l=Animals[i]
    if (len(l) ==7):
        print (l)
    i=i+1
    print (seven)