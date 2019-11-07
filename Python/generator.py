# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        # print("i : ",my_str[i])
        yield my_str[i]

# a = my_gen()
# next(a)
# next(a)
# next(a)
# next(a)
# Using for loop
# for item in my_gen():
#     print(item)  

for char in rev_str("esrever"):
    print()

my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
(x**2 for x in my_list)