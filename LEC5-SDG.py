##def cal():
##     x=10
##     y=20
##     total= x+y
##     print(total)
##
##cal()

##def cal(x,y):
##    total=x+y
##    print(total)
##cal(10,20)

##def cal():
## x=10
## y=10
## total=x+y
## return total
##
##print(cal ())

##def cal(x,y):
## total = x+y
## return total
##
##FinalTotal = cal(10,20)
##print(FinalTotal)

##def bfunc():
##    a = 99 # local variable a
##    print(a)
##
##a = 42 # global variable a
##print(a)
##bfunc()
##print(a)

##n=5
##def changeNum(n):
##    n +=5
##    print(n) #10
##changeNum(n)
##print(n) # 5

##def mysum(a,b):
##    """ Return the sum of parameters a and b. Last modified 24/09/2020 """
##    return a + b
##help(mysum)

try:
    def calculate(x,y):
        """calculate the given 2 numbers"""
        total=x+y
        print(total)
    x=float(input("Enter num 1 ="))
    y=float(input("Enter num 2 ="))
    calculate(x,y)
except Exception as e:
    print("An error has occured",e)

    
