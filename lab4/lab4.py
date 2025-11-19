from math import sqrt
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y : x * y, nums)
product2 = reduce(lambda x, y : x * y, range(1, 10))
print(product)
print(product2)


def is_prime(num) -> bool:
  if num < 1:
    return False
  if num == 1:
    return True
  for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

def prime_generator():
  num = 0
  while True:
    if is_prime(num):
      yield num
    num += 1

primes = prime_generator()
for _ in range(10): 
  print(next(primes))


numbers = [1.2, 3.4, 5.6, 7.8, 9.9 ]

rounded_numbers = map(round, numbers)
squared_rounded_numbers = map(lambda x: x*x, rounded_numbers)
print(*squared_rounded_numbers)