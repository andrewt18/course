def maximum_prime(a):
	mprime = a//2
	reslt = 1

	while mprime > 1:
		if a % mprime == 0:
			reslt = mprime
			break
		mprime -= 1

	return reslt

x = maximum_prime(3124211)
print ("MaxPrime von x = " + str(x))