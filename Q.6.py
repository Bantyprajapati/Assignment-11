n= int(input("Enter number:"))
fact=1
for i in range(2,n+1):
    fact *=i
    n-=1
print("factorial:",fact)    
