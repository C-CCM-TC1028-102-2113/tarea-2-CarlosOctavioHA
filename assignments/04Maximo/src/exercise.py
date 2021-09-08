def main():
    if x>y:
        if x>z:
            print("el número mayor es:", x)
    if y>x:
        if y>z:
            print("el número mayor es:", y)
    if z>x:
        if z>y:
            print("el número mayor es:", z)
    

print("Ingresa el primer número:")
x=int(input())
print("Ingresa el segundo número:")
y=int(input())
print("Ingresa el tercero número:")
z=int(input())
main()