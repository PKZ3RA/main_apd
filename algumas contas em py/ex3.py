produto = input("qual o nome do produto :")
valor = float(input("qual o valor que sera atribuido para este produto: "))

if valor < 10.00:
    print("produto:", produto,"valor de venda atual e de:", (valor*1.70))
elif valor >= 10.00 and valor < 30.00:
    print("produto:", produto,"valor de venda atual e de:", (valor*1.50))
elif valor >=30.00 and valor < 50.00:
    print("produto:", produto,"valor de venda atual e de:", (valor*1.40))
else:
    print("produto:", produto,"valor de venda atual e de:", (valor*1.30))