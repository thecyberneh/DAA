N=int(input("Enter Num:- "))
a=0
b=1
count=0
print(1,)

for i in range(1,N):
	count=a+b
	print(count)
	a=b
	b=count
	count=0
