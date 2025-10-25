n=int(input("enter the limit:"))
num=[]
for i in range(n):
        ele=int(input("enter the element"))
        num.append(ele)
print("the entered list:",num)
for x in num:
      if(x>0):
       print(x)
