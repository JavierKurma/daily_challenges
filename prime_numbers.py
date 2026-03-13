"""
Write a program that checks whether a number is prime or not.
Once this is done, print the prime numbers between 1 and 100.
"""
"""
-Los numeros primos son numeros mayores que 1 que son unicamente divisibles entre 1 y si mismos
"""
def is_prime_numbers(n)->bool:
    if n<=1:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True
