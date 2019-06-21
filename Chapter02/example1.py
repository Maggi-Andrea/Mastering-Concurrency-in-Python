# ch2/example1.py

from math import sqrt

import concurrent.futures
import multiprocessing

from timeit import default_timer as timer

from time import sleep

def is_prime(x):
  sleep(0.1)
  if x < 2:
    return False
  
  if x == 2:
    x
  
  if x % 2 == 0:
    return False
  
  limit = int(sqrt(x)) + 1
  for i in range(3, limit, 2):
    if x % i == 0:
      return False
  
  return x

def concurrent_solve(n_workers, input_data):
    print('Number of workers: %i.' % n_workers)

    start = timer()
    result = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_workers) as executor:

        futures = [executor.submit(is_prime, i) for i in input_data]
        completed_futures = concurrent.futures.as_completed(futures)

        sub_start = timer()

        for i, future in enumerate(completed_futures):
            if future.result():
                result.append(future.result())

        sub_duration = timer() - sub_start

    duration = timer() - start
    print('Sub took: %.4f seconds.' % sub_duration)
    print('Took: %.4f seconds.' % duration)

def main():
  input_data = [i for i in range(10 ** 13, 10 ** 13 + 1000)]
  
  for n_workers in range(1, multiprocessing.cpu_count() + 1):
      concurrent_solve(n_workers, input_data)
      print('_' * 20)

if __name__ == '__main__':
  main()

