import sys

var = -1

while var < 0:
    var = int(input("Please enter the desired position on the Fibonacci Sequence: "))

print("You entered: %d" %(var))

import array as arr
a = arr.array('d', [0])

for x in range(0, var+1):
    if x == 1:
        a.append(1)
    if x > 1:
        a.append(a[x-1] + a[x-2])

print("The value of position number %i is: %i" % (var, a[var]))

for i in reversed(a):
    print("%i" % i)

val = -1

while val < 0:
    val = int(input("Please enter the desired value on the Fibonacci Sequence: "))

for x in range(0, 1000):
    if x == 1 & len(a) == 1:
        a.append(1)
    elif x > var:
        a.append(a[x-1] + a[x-2])
    if a[x] == val:
        res = x
        break
    else:
        res = -1
        continue

if res == -1:
    print("Value not found in Fibonacci Sequence")
else:
    print("Value %d is in position %d" % (val, res))
