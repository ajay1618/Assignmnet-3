# PROGRAM TO ADD TWO NUMBERS USING CLASS AND ITS OBJECT
class Test:
    def find_sum(self, a, b):
        s = a + b
        return s


a = int(input('enter the value of a: '))
b = int(input('enter the value of b: '))
test_1 = Test()
sum = test_1.find_sum(a, b)
print(f'sum of a and b is: {sum}')




