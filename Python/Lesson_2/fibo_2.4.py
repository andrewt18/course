def fibo(n):
	if n == 0: return 0
	if n == 1: return 1
	return fibo(n - 1) + fibo(n - 2)

def fibo2(n):
	if n == 0: return 0
	if (n == 1) or (n == 2): return 1

	pre = 1
	fib = 1
	sled = pre + fib
	while n > 3:
		pre = fib
		fib = sled
		sled = pre + fib
		n -= 1
	return sled


x = fibo2(50)
print(x)