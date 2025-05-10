import math
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a == 0:
    print("Não é equação do segundo grau")
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Não há raízes reais")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes da equação são: x1 = {x1:.2f} e x2 = {x2:.2f}")
