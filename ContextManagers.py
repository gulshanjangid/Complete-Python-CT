class MyContext:

    def __enter__(self):
        print("Entering")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")


with MyContext():
    print("Inside")