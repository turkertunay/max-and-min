aa = input("enter first number: ")
bb = input("enter second number: ")
cc = input("enter third number: ")

a = int(aa)
b = int(bb)
c = int(cc)

def max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b>= c:
        return b
    else:
        return c

print("The biggest number is: ", max(a, b, c))

def min(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b<= c:
        return b
    else:
        return c

print("The smallest number is: ", min(a, b, c))



