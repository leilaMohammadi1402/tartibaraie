print("Enter your numbers and 'end' at the end.")

List = []
userNum = input("Enter your number: ")
while userNum != 'end':
    List.append(userNum)
    userNum = input("Enter your number: ")

print("list;",List)

a=List
n=len(a)
for i in range(1,n):
    if a[i-1]<a[i]:
        print("kalamat   betartib hastan")
    else:
        print("no")
        print("hala ke iek no vojod darad be tartib ((( nist !!!!!!)))")

List.sort()
print("shekl sahih:",List)