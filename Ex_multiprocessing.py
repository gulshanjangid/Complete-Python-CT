from multiprocessing import Process


def task(name):
    print(f"{name} is running")


if __name__ == "__main__":

    p1 = Process(target=task, args=("Task 1",))
    p2 = Process(target=task, args=("Task 2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All tasks completed")