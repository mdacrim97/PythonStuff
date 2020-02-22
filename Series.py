from threading import Lock
import multiprocessing
import math


class Series():
    def __init__(self):
        self.lock = Lock()
        self.result = 0.0
        

    def sumThread(self, i, n, functionToSum, x):
        sum=0.0
        for t in range(i, n+1):
            sum += functionToSum(x)

        self.lock.acquire()
        print(sum)
        self.result += sum
        self.lock.release()

    def summation(self, i , n , functionToSum, x):
        threads = []

        for t in range(0, multiprocessing.cpu_count()):
            #seperate chunks of series for each thread range.
            newThread = multiprocessing.Process(target=self.sumThread, args=(i, n, functionToSum, x))
            threads.append(newThread)
            newThread.start()

        for thread in threads:
            thread.join()

        return self.result


def Weierstrauss(x):
    return (.5**x) * math.cos((11**math.pi * x))

A = Series()
print(A.summation(0, 1000, Weierstrauss, 7))



