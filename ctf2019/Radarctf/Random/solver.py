key =int(chr(102 - 49))
print(key)
a = [109,92,95,92,109,118,109,92,105,95,90,100,110,90,105,106,111,90,98,106,106,95,90,100,95,96,92,90,103,106,103,120]
s = ''
for j in range(len(a)):
	s+=chr(a[j]+key)
print(s)