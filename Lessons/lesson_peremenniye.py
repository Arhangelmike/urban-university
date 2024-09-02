
inputs_int=input("Enter number: ")
a = 78
b = 654
c = 865
R = 'sum('
if int(inputs_int) <= 100:
    e = a + b
else:
    e = c / b
if e >= a:
    print(R)
    R = R + str(e)
    print(R)
else:
    print(R)
    R = R + str(a) + '*' + str(c)
    print(R)


R = R + ')'

print(f'{R}')