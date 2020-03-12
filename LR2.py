#!/usr/bin/env python
# coding: utf-8

# In[1]:


i = 0
x = 0
y = 0
while 1:
  a = int(input("Введите числo: "))
  if a == 0:
    print ("Сумма положительных чисел = ", x)
    print ("Сумма отрицательных чисел = ",y)
    break
  else:
    if a > 0:
      x +=a
    else:
      y +=a


# In[2]:


firstNumber = 1
secondNumber = 1
sumNumbers = 0
print (firstNumber, secondNumber, end = " ")
while sumNumbers < 21:
  sumNumbers = firstNumber + secondNumber
  print (sumNumbers, end = " ")
  firstNumber = secondNumber
  secondNumber = sumNumbers

    
    


# In[ ]:


a = 0
b = 1000
for i in range (10):
  x = int(input("Введите число от 0 до 1000: "))
  if 0 <= x <= 1000:
    if (x % 2 == 0) and (x % 3 != 0):
      a = x
      if a < b:
        b = a
  else:
    print ("Вы ввели некорректное число")
print (b) 


# In[1]:


sumNumbers = 0
x = int(input("Введите количество элеметов: "))
for i in range (x):
  y = int(input("Введите число: "))
  sumNumbers = sumNumbers + y
b = sumNumbers/x
print ("Среднее арифметическое = ", b)


# In[3]:


from random import randint

sumNumbers = 0

x = int(input("Введите количество элеметов: "))

for i in range (x):

    y = randint(1, 100)

    print (y)

    sumNumbers = sumNumbers + y

b = sumNumbers/x

print ("Среднее арифметическое = ", b)


# In[4]:


for num in range(100,10000):
  sum = 0
  temp = num
  n = len(str(num))
  while temp > 0:
          d = temp % 10
          sum += d ** n
          temp //= 10
  if num == sum:
      print(num)


# In[5]:


n=int(input("Введите число "))

for i in range(n+1):

    s=str(i)

    l=len(s)

    s2=str(i*i)

    if s2[-l:]==s:

        print(i)


# In[6]:


i = 1

for day in 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье':

    if i==6 or i == 7:

        print (i,'-й день недели - это: ', day, '- выходной день')

    else:

        print (i,'-й день недели - это: ', day, '- рабочий день')

    i+=1


# In[ ]:




