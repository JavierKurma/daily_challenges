"""
Write a program that prints the first 50 numbers of the Fibonacci
sequence starting from 0.
- The Fibonacci series is composed of a sequence of numbers in
  which the next one is always the sum of the previous two.
  0, 1, 1, 2, 3, 5, 8, 13...

"""
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print("Cuantos numeros de Fibonacci desea ver?")
x=int(input("->"))
while not isinstance(x,int):
    print("Ingrese un numero")
    x=int(input("->"))

"""for i in range(x):
    if i==x-1:
        print(fibonacci(i))
    else:
        print(fibonacci(i), end=", ")"""

#Let's see how to optimize the Fibonacci series with a generator
#We should create a generator that calls Fibonacci each time and then stores the value:
def fibonacci_generador():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

gen=fibonacci_generador()
for i in range(x):
    print(next(gen))


