"""
Write a program that checks whether a number is prime or not.
Once this is done, print the prime numbers between 1 and 100.
"""
"""
-A prime number is all that is greatter than 1 and it only have %0 by 1 and itself
"""
def is_prime_numbers(n)->bool:
    if n<=1:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True
print("Input the range that you want to veriify prime numbers:")
x=(input("->"))
while True:
    try:
        x=int(x)
        break
    except:
        while not isinstance(x,int):
            print("Ingrese un numero entero")
            x=(input("->"))
for i in range(x):
    if is_prime_numbers(i):
        print (f"{i}",end=" ")
print("")

#Prime numbers are important for cibersecurity on encriptation


