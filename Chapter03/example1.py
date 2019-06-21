# ch3/example1.py

from Chapter03.my_thread import MyThread

import _thread as thread

thread1 = MyThread('A', 0.5)
thread2 = MyThread('B', 0.5)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


print('Finished.')
