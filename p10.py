def simple_intrest(p,t,r) :
    s=float((p*r*t)/100)
    print("Simple intrest is ",s)

p=int(input("Enter principal amount : "))
r=float(input("Enter intrest rate (in %) : "))
t=int(input("Enter time : "))
simple_intrest(p,t,r)
