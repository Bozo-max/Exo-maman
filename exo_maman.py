from math import sqrt, pow, log

def Briggs(x, p):
    n = 0
    while abs(x - 1) > p:
        x = sqrt(x)
        n += 1
    return (x - 1) * pow(2, n)


print("Briggs(2,10^-3) = ", Briggs(2, 1e-3))
print("ln(2) = ", log(2))
print("Briggs(0.8,10^-3) = ", Briggs(0.8, 1e-3))
print("ln(0.8) = ", log(0.8))
print()


for n in range(3, 8):
    print("Briggs(2,10^",-n,") = ", Briggs(2, pow(10,-n)), sep="")
    print("Briggs(2,10^", -n, ") - ln(2)= ", Briggs(2, pow(10, -n))-log(2), sep="")
    print()
