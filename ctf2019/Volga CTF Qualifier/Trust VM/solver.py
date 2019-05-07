const = [0xE1, 0xA9, 0xE1, 0x2E, 0x0B, 0x15, 0x44, 0x9C, 0x08, 0xDC, 0xDC, 0xF3, 0x1A, 0x91, 0x9C, 0x6E, 0x34, 0x5C, 0xE4, 0x5E, 0xF9, 0xE2, 0x5F, 0xF1, 0xF0, 0x86, 0x05, 0xA8, 0x70, 0x6E, 0x04, 0x53, 0x9D, 0x31, 0xEC, 0x10, 0xAB, 0xEA, 0xF6, 0x74, 0x44, 0x79, 0x0F, 0x28, 0x53, 0x40, 0x37, 0x2C, 0x17, 0x9A, 0xC3, 0x67, 0x95, 0x2F, 0x4B, 0x27, 0xD9, 0x3F, 0xF9, 0x1D, 0x2A, 0x70, 0x77, 0x5D]
def fun(A,n):
    temp = []
    for i in range(64):
        temp.append(0)
    off = n>>3
    r = n&7
    for i in range(64):
        temp[(off+i)&0x3f] = (A[(i-1)%64]>>(8-r))|(A[i]<<r)&0xff
    return temp

def defun(A,n):
    t = []
    off = n>>3
    r = n&7
    for i in range(64):
        t.append(0)
    for i in range(64):
        t[(i-off)&0x3f] = ((A[(i+1)%64]<<(8-r))|(A[i]>>r))&0xff
    return t

f = open('data.enc','rb')
g = open('data.png','wb')
for i in range(5271):
    A = f.read(64)
    A = list(map(ord, A))
    B = A
    A = defun(A,0x4d)
    s = ''
    for i in range(64):
        A[i] ^= const[i]
        s+=chr(A[i])
    g.write(s)
    const = fun(const,0x6f)
    for i in range(64):
        const[i]^=A[i]
    
