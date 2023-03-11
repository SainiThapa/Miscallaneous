import math
def gcd(m,n):
    if m==0:
        return n
    if n==0:
        return m
    else:
        return gcd(n,m%n)

def encryption(m,e,n):
    c=pow(m,e)%n
    return c
def decryption(c,d,n):
    m=pow(c,d)%n
    return m

print("Enter two prime numbers p and g:")
a=int(input("Enter value of p: "))
b=int(input("Enter value of g: "))
n=a*b
phi=(a-1)*(b-1)
for e in range(2,phi):
    if(gcd(phi,e)==1):
        break;
d=0
while((e*d)%phi!=1):
    d=d+1
print("Public key: {",e,",",n,'}')
print("Private key: {",d,",",n,"}")
m=int(input("Enter your message in number format: "))
print("Plaintext: ",m)
print("Ciphertext: ",encryption(m,e,n))
c=encryption(m,e,n)
print("\nAfter decryption: ",decryption(c,d,n))