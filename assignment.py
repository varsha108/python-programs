def myinput():
    a=int(input("enter a"))
    b=int(input("enter b"))
    return a,b
def mysum(a,b):
    return a+b
def myprint(a,b, mysum):
    print("%d + %d = %d", (a,b, mysum))
def main():
    a, b=myinput()
    s=mysum(a,b)
    myprint(a,b,s)

