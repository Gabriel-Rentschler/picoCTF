import sys

flag = open(sys.argv[1],'r')

flag = flag.read()

for i in range(0, len(flag)):
    r=ord(flag[i])>>8
    print(chr(r), end='')
    u=ord(flag[i])-(r<<8)
    print(chr(u), end='')

