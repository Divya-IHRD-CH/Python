curr=int(input("enter the current year:"))
fut=int(input("enter the future year:"))
print("leap years:")
flag=0
for curr in range(curr,fut+1):
 if((curr%4==0) and curr%100!=0 or curr%400==0):
    print(curr)
 else:
    flag=1
if flag==1:
    print("no leap year")
