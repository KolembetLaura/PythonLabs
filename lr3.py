	3.1.1
def difference(): 
  print ("Разность чисел = ", a-b) 
a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
difference()

3.1.2
def difference(a,b): 
  print ("Разность чисел = ", a-b)
num1 = int(input("Введите 1 число: "))
num2 = int(input("Введите 2 число: "))
difference(num1, num2)

3.2 
def number():
  n1 = int(input("Введите целое число: "))
  n2 = 0
  while n1 > 0:
    digit = n1 % 10; # находим остаток - последнюю цифру числа
    n1 = n1 // 10; # делим нацело - убираем из числа последнюю цифру
    n2 = n2 * 10 # увеличиваем разрядность второго числа
    n2 = n2 + digit # добавляем очередную цифру
  for i in str(n2):
    print(i)
number()

3.3
def print_factors(x):
  print("Делителями числа",x,"являются:") 
  for i in range(1, x + 1): 
    if x % i == 0: 
      print(i) 
num = int(input("Введите число: "))
print_factors(num) 


3.4

def difference(a,b): 
  print ("Степень числа = ", a**b)
num1 = int(input("Введите число: "))
num2 = int(input("Введите степень числа: "))
difference(num1, num2)






3.5

def Fib(n):
  f1 = f2 = 1
  i = 0
  while (i < n):
    i += 1
    s = f1 + f2
    f1 = f2
    f2 = s
    print(s)
Fib(int(input("Введите число: ")))

3.6
def kolvo(n):
  kol = len (str(n))
  return kol
print(kolvo(int(input("Введите число: "))))

3.7

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
print (factorial(int(input("Введите число: "))))





