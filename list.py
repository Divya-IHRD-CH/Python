list1=[]
list2=[]
m=int(input("ENTER THE LIMIT OF LIST1:"))
print("Enter the elements:")
for i in range(0,m):
      value=int(input())
      list1.append(value)
n=int(input("ENTER THE LIMIT OF LIST2:"))
print("Enter the elements:")
for i in range(0,n):
      value=int(input())
      list2.append(value)
print(list1,list2)
if len(list1)==len(list2):
                   print("Both list1 and list2 are of same length")
else:
    print("Both list1 and list2 are  NOT of same length")
if sum(list1)==sum(list2):
    print("The sum of both list1 and list2 are of same ")
else:
    print("The sum of both list1 and list2 are NOT same ")
list3=[each for each in list1 if each in list2]
print("Same Members are:",list3)
    
    
    
