a = True
b = False

c = a and b
d = a or b
e = not a and not b

if (c):
    print("c")
elif (d):   # else if
    print("d")
else:
    print("e")
# end of da else

for i in range(1,10):
    print(i)

# list (seznam) - ekvivalent pole
pole = [1,3,5,7,9,11,13,15,17,19]
for i in pole:  # tzv. for-each
    print(i)

for i in range(0,10):   # 'obyč' for
    print(pole[i])

for i in range(0, len(pole)):
    print(pole[i])

# udělejte cyklus, který:
# - projde všechna čísla od 1 do 100
# - vypíše lichá čísla normálně
# - místo sudých čísel vypíše 'T_T'

for i in range(0, 100+1):
    if (i % 2 == 0):  # sudý
        print("T_T")
    elif (i % 2 == 1):
        print(i)
    else:
        print("Toto nemůže nikdy nastat")