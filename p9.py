n1=int(input("Enter marks of subject 1 out of 100 : "))
n2=int(input("Enter marks of subject 2 out of 100 : "))
n3=int(input("Enter marks of subject 3 out of 100 : "))
n4=int(input("Enter marks of subject 4 out of 100 : "))
n5=int(input("Enter marks of subject 5 out of 100 : "))
s=n1+n2+n3+n4+n5
print("Mean = ",s)
p=s*100/500
print("Percentage = ",p)
if p<35 :
    print("Fail!!!")
else :
    print("Pass!!!")

