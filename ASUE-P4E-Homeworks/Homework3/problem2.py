num = int(input("Enter a positive integer: "))

def asked_primes(number):
	primes = []
	for i in range(2, number+1):
		isPrime = True
		for number in range(2, int(i ** 0.5)+1):
			if i % number == 0:
				isPrime = False
		if isPrime:
			primes.append(i)
	return primes

primes = asked_primes(num)
for j in range(len(primes)):
	print(primes[j], end=' ')

