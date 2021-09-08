def main():
    if x>y>z:
        print(z)
        print(y)
        print(x)
    if y>x>z:
        print(z)
        print(x)
        print(y)
    if z>x>y:
        print(y)
        print(x)
        print(z)
    if x>z>y:
        print(y)
        print(z)
        print(x)
    if y>z>x:
        print(x)
        print(z)
        print(y)
    if z>y>x:
        print(x)
        print(y)
        print(z)

print("Ingresa el primer número:")
x=int(input())
print("Ingresa el segundo número:")
y=int(input())
print("Ingresa el tercero número:")
z=int(input())
main()