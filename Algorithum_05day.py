
name="v i n a y v"
l=[]
for value in name.split():
    l.append(value)

print(l)

d=dict()
for value in l:
	if value in d:
		d[value]=d[value]+1
	else:
		d[value]=1

for key, value in d.items():
	if value == 2:
		print(key)
	
		

