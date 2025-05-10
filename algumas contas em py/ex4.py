num1 = float(input("digite um numero:"))
num2 = float(input("digite um numero:"))
print("escolha as opcoes a seguir")
print("1. soma")
print("2. divisao")
print("3. subtracao")
print("4. multiplicacao")
opcao = input("digite a opcao desejada: ")

if opcao == 1:
    print("o Resultado da soma e: ", (num1+num2) )
elif opcao == 2:
    print("o Resultado da divisao e: ", (num1/num2) )
elif opcao == 3:
    print("o Resultado da subtracao e: ", (num1-num2) )
else:
    print("o Resultado da multiplicacao e: ", (num1*num2) )
    