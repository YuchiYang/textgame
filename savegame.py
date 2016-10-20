__author__ = 'Smaran'

def encrypt(vals,passw):
    n=0
    s=''
    for i in range (3):
        n=encode(vals[i])
        n[0]=(n[0]*passw)%26
        n.append(n[0]/26)
        n[1]=(n[1]*passw)%26
        n.append(n[1]/26)
        s+=chr(n[0])+chr(n[1])


    filename = passw+"newfile.txt"

    passw=encode(passw)
    enc= n*passw

    enc=str(enc)
    # Open the file with writing permission
    myfile = open(filename, 'w')

    # Write a line to the file
    myfile.write(enc)

    # Close the file
    myfile.close()

def encode(s):
    a=s%26
    b=s/26
    c=[a,b]
    print(c,chr(b),chr(a))

    return c

def decrypt(pasw):
    filename = "newfile.txt"
    s=0
    # Open the file as f.
    # The function readlines() reads the file.
    with open(filename) as f:
        content = f.readlines()

    for line in content:
        for i in line:
            print(i)
            s+=i
        # print(line,end='')
    s=s/pasw

a='a'
b='b'
c=a+b
print(c)
