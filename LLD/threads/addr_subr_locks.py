import threading



global shared_var
# lock = threading.Lock()


def addr(n):
    global shared_var
    for i in range(n):
        # lock.acquire()
        shared_var += 1
        # lock.release()

def subr(n):
    global shared_var
    for i in range(n):
        # lock.acquire()
        shared_var -= 1
        # lock.release()



shared_var = 0
n = 1000000

t1 = threading.Thread(target=addr, args=(n,))
t2 = threading.Thread(target=subr, args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()
print(shared_var)
