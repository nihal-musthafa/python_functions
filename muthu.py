num1=int(input("Enter a number : "))
num2=int(input("enter a number :"))
print(num1,num2)
operator=input("enter a operator(+,-,*,/,%) (1,2,3,4,5)")
print(operator)
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def mod(num1,num2):
    return num1%num2
if operator=="1":
    result=add(num1,num2)
    print(result)
