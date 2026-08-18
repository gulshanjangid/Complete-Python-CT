# def my_decorator(func):

#     def wrapper():
#         print("Starting...")

#         func()

#         print("Finished...")

#     return wrapper
# @my_decorator
# def greet():
#     print("Hello Gulshan")


# # greet = my_decorator(greet)

# greet()

def check_login(func):

    def wrapper():
        print("Checking login...")
        func()

    return wrapper

@check_login
def add():
    print("Adding data")


@check_login
def delete():
    print("Deleting data")

add()
delete()