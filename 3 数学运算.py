import math

"函数1-add：相加"
def add(x, y):
   return x + y

"函数2-subtract：相减"
def subtract(x, y):
   return x - y
 
"函数3-multiply：相乘"
def multiply(x, y):
   return x * y

"函数4-divide：相除"
def divide(x, y):
   return x / y

"函数5-modulus_operation：取模" 
def modulus_operation(x,y): 
    return x % y

"函数6-exponentiation：幂运算" 
def exponentiation(x,y):
    return x ** y

"函数7-gcd:最大公约数"
def gcd(x,y):
    return math.gcd(x,y)

"函数8-Fibonacci_sequence：斐波那契数列"
def Fibonacci_sequence(n):
    a,b,fn = 1,1,1
    sn = 1 if n == 1 else 2
    count = 3
    while count <= n:
        fn = a + b 
        a = b
        b = fn
        sn = sn + fn
        count = count + 1
    return "F(%d) = %d" %(n,fn),"S(%d) = %d" %(n,sn)

print("选择运算：")
print("1 相加")
print("2 相减")
print("3 相乘")
print("4 相除")
print("5 取模")
print("6 幂运算")
print("7 最大公约数")
print("8 斐波那契数列")
 
choice = input("输入你的选择(1/2/3/4/5/6/7/8):")

 
if choice == '1':
   num1 = int(input("输入第一个数字: "))
   num2 = int(input("输入第二个数字: "))
   print(num1,"+",num2,"=", add(num1,num2))
 
elif choice == '2':
   num1 = int(input("输入第一个数字: "))
   num2 = int(input("输入第二个数字: "))
   print(num1,"-",num2,"=", subtract(num1,num2))
 
elif choice == '3':
   num1 = int(input("输入第一个数字: "))
   num2 = int(input("输入第二个数字: "))
   print(num1,"*",num2,"=", multiply(num1,num2))
 
elif choice == '4':
   num1 = int(input("输入第一个数字: "))
   num2 = int(input("输入第二个数字: "))
   print(num1,"/",num2,"=", divide(num1,num2))
   
elif choice == '5':
   num1 = int(input("输入第一个数字: "))
   num2 = int(input("输入第二个数字: "))
   print(num1,"%",num2,"=", modulus_operation(num1,num2))
   
elif choice == '6':
   num1 = int(input("输入第一个数字: "))
   num2 = int(input("输入第二个数字: "))
   print(num1,"^",num2,"=", exponentiation(num1,num2))
   
elif choice == '7':
   num1 = int(input("输入第一个数字: "))
   num2 = int(input("输入第二个数字: "))
   print(num1,"和",num2,"的最大公约数是", gcd(num1,num2))
   
elif choice == '8':
   num1 = int(input("输入项数: "))
   print(Fibonacci_sequence(num1))
else:
   print("非法输入")
