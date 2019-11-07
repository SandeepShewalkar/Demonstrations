def decorator123(func):
    def wrapper():
        print("Data logging started")
        func()
        print("Data logging done")
    return wrapper

@decorator123
def login():
    print("This is login func")

# login()


# login = decorator(login)

login()