gach="--------------------------------------------------"
print ("CHUONG TRINH XAC DINH TAM GIAC VA TINH CHU VI-DIEN TICH")

print (gach)
a=float(input("Nhap vao canh a: "))
b=float(input("Nhap vao canh b: "))
c=float(input("Nhap vao canh c: "))

if (a+b>c) & (b+c>a) & (a+c>b) & (a>0) & (b>0) & (c>0):
    if (a==b)&(b==c):
        print ("Day la tam giac deu")
    elif (a==b)& (a!=c) | (a==c)&(a!=b) | (b==c) & (b!=a):
            print ("Day la tam giac can")
    elif (a*a==b*b+c*c)|(b*b==a*a+c*c)|(c*c==a*a+b*b):
            print("Day la tam giac vuong")
    else:
        print("Day la tam giac thuong")
    import math
    cv=a+b+c
    p=cv/2
    dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print ("Chu vi tam giac : ",round(cv,2))
    print ("Dien tich tam giac : ",round(dt,2))
else:
        print ("Khong tao thanh tam giac")
print (gach)
print ("Thank You ")
