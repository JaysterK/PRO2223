# řešitel kvadratické rovnice y = ax^2+bx+c
import math, cmath

def discriminant(a,b,c):
    return float(b ** 2 + (-4 * a * c))

def quadratic_equation(a,b,dis):
    vysledek1 = (-b + math.sqrt(dis)) / (2 * a)
    vysledek2 = (-b - math.sqrt(dis)) / (2 * a)
    return vysledek1,vysledek2

def imaginary_quadratic_equation(a,b,dis):
    vysledek1 = (-b + cmath.sqrt(dis)) / (2 * a)
    vysledek2 = (-b - cmath.sqrt(dis)) / (2 * a)
    return vysledek1,vysledek2

print("""Yo, I'm your quadratic calculator just give me a, b, and c and I will do 
everything for you(quadratic equation looks like this btw: ax^2 + bx + c).\n""")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if(a == 0):
    if(b == 0):
        print("Ky5")

    tits = c/-b
    print(tits)
else:
    dis = discriminant(a,b,c)

    if(dis == 0):
        vysledek = float(-b/(2*a))
        print("\nDiscriminant is equal to zero therefore we have one answer.")
        print(vysledek)
    elif(dis > 0):
        print("\nDiscriminant is positive therefore we have two results.")
        vysledek = quadratic_equation(a, b, dis)
        print(vysledek)
    else:
        print("\nDiscriminant is negative so we have results in imaginary numbers.")
        vysledek = imaginary_quadratic_equation(a, b, dis)
        print(vysledek)
