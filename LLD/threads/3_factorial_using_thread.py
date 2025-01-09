import math
import threading


# Todo: implement the factorial thread class
class FactorialThread(threading.Thread):
    # write code here
    def __init__(self, n):
        super().__init__()
        self.n = n
    
    def run(self):
        self.result = math.factorial(self.n)


    


def compute_large_factorial(n):
    factorial_thread = FactorialThread(n)
    factorial_thread.start()

    factorial_thread.join()

    return factorial_thread.result
    

if __name__ == "__main__":
    print(compute_large_factorial(10))