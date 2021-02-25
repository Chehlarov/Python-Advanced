import logging
from functools import lru_cache

logging.basicConfig(filename='demo-logs.log', level=logging.DEBUG)


@lru_cache()
def fibonacci(n):
    if n == 0:
        logging.debug('Calculating fibonacci 0')
        return 0
    if n == 1:
        logging.debug('Calculating fibonacci 1')
        return 1
    prev_fib = fibonacci(n - 1)
    logging.debug(f'prev_fib = {prev_fib}')
    two_prev_fib = fibonacci(n - 2)
    logging.debug(f'two_prev_fib = {two_prev_fib}')
    return prev_fib + two_prev_fib


n = int(input())
print(fibonacci(n))
