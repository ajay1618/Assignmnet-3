# swap function to swap two variables
def swap(a, b):
    temp = a
    a = b
    b = temp
    return f'new value of a is: {a} \nnew value of b is: {b}'


a = int(input('enter value of a: '))
b = int(input('enter value of b: '))
print(swap(a, b))
