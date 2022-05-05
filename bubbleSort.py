def bubbleSort(arr):
	n=len(arr)

	for i in range(n-1):
		for j in range(0,n-i-1):

			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]



arr=[12, 45, 18, 9, 6, 78]
print("This arr is:- ")
print(arr)
bubbleSort(arr)
print("New arr is:- ")
print(arr)
