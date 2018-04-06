#Prime number 
def prime_num(X):
	for i in range(2,X):
		if X % i == 0:
			return False
	return True

print(prime_num(15))

		


