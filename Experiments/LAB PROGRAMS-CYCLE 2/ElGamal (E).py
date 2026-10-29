p,g,x=23,5,6
y=pow(g,x,p)
m,k=12,3
a=pow(g,k,p)
b=m*pow(y,k,p)%p
d=b*pow(pow(a,x,p),p-2,p)%p
print("Encrypted:",a,b)
print("Decrypted:",d)
