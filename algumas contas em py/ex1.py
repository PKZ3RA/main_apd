idade = int(input("qual dua idade: "))
if idade < 16:
    print("voce nao e um eleitor pois tem ", idade)
elif idade >=18 and idade <=65:
    print("voce e um eleitor obrigatorio")
else:
    print("voce e um eleitor facultativo cuja a idade e de", idade, "nao obriga o direito de cidadao" )