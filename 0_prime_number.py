def prime_number(n):
    prime_number_list = []

    for c in range(2,n+1):
        is_prime_number = True
        for i in range(2, c):
            if c%i == 0:
                is_prime_number = False
                break

        if is_prime_number:
            prime_number_list.append(c)

    return prime_number_list

print(len(prime_number(10000)))


def optimized_prime_number(n):
    
    prime_number_list = []
    filter_list = []

    for c in range(2,n+1):
        is_prime_number = True

        for i in filter_list:
            if c%i == 0:
                is_prime_number = False
                break

        if is_prime_number:
            prime_number_list.append(c)
            if c**2 < n:
                filter_list.append(c)

    return prime_number_list



N = 20000

from time import time 

tick1 = time()
prime_number(N)
tick2 = time()
optimized_prime_number(N)
tick3 = time()

print('prime number time: ', (tick2 - tick1) * 1000, 'ms')
print('opt prime number time: ', (tick3 - tick2) * 1000, 'ms')

print(len(optimized_prime_number(10000)))
