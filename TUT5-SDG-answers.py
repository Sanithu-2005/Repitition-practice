#Excercise 1

##Part A
hidden=6
try:
    number=int(input("Enter a number between 1 and 20"))
    if number>1 and number<20:
        while number != hidden:
            print("Not correct guess. Guess again")
            number=int(input("Enter a number between 1 and 20"))
        print("Your guess = ",number,"is correct")
        
    else:
        print("Beyond limit.Enter a number between 1 and 20")
except Exception as e:
    print("An error has occured",e)

##Part B
import random
hidden=random.randint(2,19)
print("The Hidden number is",hidden)
try:
    number=int(input("Enter a number between 1 and 20"))
    if number>1 and number<20:
        while number != hidden:
            print("Not correct guess. Guess again")
            number=int(input("Enter a number between 1 and 20"))
        print("Your guess = ",number,"is correct")
        
    else:
        print("Beyond limit.Enter a number between 1 and 20")
except Exception as e:
    print("An error has occured",e)

##Part C
import random
hidden=random.randint(2,20)
print("The Hidden number is",hidden)
try:
    number=int(input("Enter a number between 1 and 20"))
    if number>1 and number<20:
        while number != hidden:
            print("Not correct guess. Guess again")
            if number>hidden:
                print("Your guess is too low")
            elif number<hidden:
                print("Your guess is too high")
            number=int(input("Enter a number between 1 and 20"))
        print("Your guess = ",number,"is correct")
        
    else:
        print("Beyond limit.Enter a number between 1 and 20")
except Exception as e:
    print("An error has occured",e)
##

##Exercise 2
total = 0 # sum of scores
count = 0 # number of scores entered
average=0
score = float(input("Enter score, (Enter -9 to end): ") )
while score!=-9:
    total+=score
    count+=1
    score = float(input("Enter score, (Enter -9 to end): ") )
average= float(total)/count
print("Class average is", average)

##Excercise 3
n=0
while n==0:
        n = input("Please enter an integer: ")
        try:
            n = int(n)
            continue
        except ValueError:
            print("Requires a valid integer! Please try again.")
            print("You successfully entered an integer.")


##Excercise 4
total=0
for i in range (1,6):
    total+=i
print(total)

##Excercise 5
for i in range (1,20,2):
    print(i)

##Excercise 6
num=int(input("Enter number of stars"))
for i in range (num):
    print("*")

##Excercise 7
import random
count=0
for i in range(1,101):
    roll_1=random.randint(1,7)
    roll_2=random.randint(1,7)
    if roll_1==roll_2:
        count+=1
print("Out of 100 you rolled",count,"doubles.")

##Excercise 8
for number in range(3) :
print("-------------------------------------------")
print("Outer loop iteration " + str(number))
# Inner loop for
another_number in range(4):
print("****************************")
print("In inner loop iteration " + str(another_number))

for x in range(1,4):
    for y in range(1,4,2):
        print('*', end='') 
