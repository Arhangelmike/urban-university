import os, sys, time
os.system('color')
os.system('cls')

a = 1
R = '\x1b['
i = 28
while a == 1:
    i += 1
    R = R + str(i) + 'm'
    print(f'{R} + Success! + {R} +')
    sys.stdout.flush()
    R = '\33['
    time.sleep(1)
    if i == 100:
        break