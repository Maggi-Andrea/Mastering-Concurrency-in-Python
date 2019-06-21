# ch1/example2.py

import concurrent.futures
from timeit import default_timer as timer

max_iter = 20

result = 3

# sequential
def f(x):
  return x * x - x + 1

def process_sequential():
  global result
  start = timer()
  result = 3
  for i in range(max_iter):
    result = f(result)
  
  print('Sequential Result is very large. Only printing the last 5 digits:', result % 100000)
  print('Sequential took: %.2f seconds.' % (timer() - start))

import threading

rlock = threading.Lock()

# concurrent
def concurrent_f(x):
  global result
  print('concurrent_f', x, result % 100000)
  result = f(result)

def process_concurrent():
  global result
  start = timer()
  result = 3
  with concurrent.futures.ThreadPoolExecutor(max_workers=max_iter) as exector:
    futures = [exector.submit(concurrent_f, i) for i in range(max_iter)]
    _ = enumerate(concurrent.futures.as_completed(futures))
     
  print('Concurrent Result is very large. Only printing the last 5 digits:', result % 100000)
  print('Concurrent took: %.2f seconds.' % (timer() - start))

if __name__ == '__main__':
  process_sequential()
  process_concurrent()

