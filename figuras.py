def mdc(dividendo, divisor):
    if (divisor == 0):
        return dividendo
    else:
        return mdc(divisor, dividendo % divisor)


x = int(input())


for i in range(1, x + 1):
	f1 = input().split()
	a = int(f1[0])
	b = int(f1[1])
	print(mdc(a,b))
