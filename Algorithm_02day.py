
a=[1,2,3,5,8,0]

#code for finding minimum
a.sort()
a[0]
print(a[0])


#Second approch


min_var=a[0]
for value in a:
	print(value)
	if min_var > value:
		min_var=value


#Minimum of array
print(min_var)

X=[2,5,6,4,8,9,1,3]


for i in range(len(X)):
	if i >= 2 and i <= 4:
		print (X[i])


X=[2,3,5,6,1,1,8,9,4,2,6]
for i in range(len(X)):
	X[i]=X[i]+1
	print (X[i])


import math

X=[2,1,3]
def std(X):
	sum = 0
	for value in X:
		sum = sum + value

	mean=sum/len(X)
	print(mean)
	sd=0

	for value in X:
		sd = sd + ((value - mean)**2)/len(X)
	return math.sqrt(sd)

print(std(X))




#Table of num
def table_fun(value):

	for n in range(11):
		prod=value*n
		print(prod)

table_fun(10)





#Eveb Multiple of 15
for n in range(150):
	if n % 15 == 0 and n % 2 == 0:
		print(n)






	






