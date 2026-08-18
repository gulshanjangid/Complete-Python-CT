import threading
import time

def task1():
    time.sleep(2)
    print("Task1 is  completed")

def task2():
    time.sleep(2)
    print("Task2 is  completed")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks completed")


