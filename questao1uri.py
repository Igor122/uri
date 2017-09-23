def mdc(dividendo, divisor):
    if divisor == 0:
        return dividendo
    else:
        return mdc(divisor, dividendo % divisor)


x = int(input("Digite o numero de rodadas\n"))


for i in range(1, x + 1):
	print("Rodada %d \n" % i)
	f1 = int(input("Digite o valor de F1\n"))
	f2 = int(input("Digite o valor de F2 \n"))
	print(mdc(f1,f2))
