from contextlib import contextmanager


@contextmanager
def my_context():

    print("Start")

    yield

    print("Cleanup")


with my_context():
    print("Hello")