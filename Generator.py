def my_generator():
    print("First")
    yield 10

    print("Second")
    yield 20

    print("Third")
    yield 30

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))