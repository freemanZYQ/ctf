a=[153,176,135,158,112,232,65,68,5,4,139,154,116,188,85,88,181,97,142,54,172,9,89,229,97,221,62,63,185,21,237,213]
for i in range(4):
    for j in range(1,32)[::-1]:
        a[j]^=a[j-1]
s=''
for i in range(32):
    a[i]^=i
    a[i]=((a[i]>>2)|(a[i]<<6))&0xff
    s+=chr(a[i])
print(s)