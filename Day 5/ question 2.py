# Question 2
# Make a Function for prime numbers and use Filter to filter out all the prime numbers from 1-2500


def CheckPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            return (num)


prime_nums = list(filter(CheckPrime, list(range(1, 2500))))
print(prime_nums)
