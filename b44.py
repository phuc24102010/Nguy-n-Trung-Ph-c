n=int(input())
if (n%4==0 and n%100!=0) or n%400==0:
    print("Nam nhuan")
else:
    print("Khong phai nam nhuan")