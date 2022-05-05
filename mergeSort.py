def mergeSort(arr):
	if len(arr) > 1:
		mid=len(arr)//2

		L=arr[:mid]
		R=arr[mid:]

		mergeSort(L)
		mergeSort(R)

		i=j=k=0

		while i < len(L) and j < len(R):

			if L[i] < R[j]:
				arr[k]=L[i]
				i+=1

			else:
				arr[k]=R[j]
				j+=1
			k+=1

		while i < len(L):
			arr[k]=L[i]
			i+=1
			k+=1

		while j < len(R):
			arr[k]=R[j]
			j+=1
			k+=1

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


if __name__=='__main__':
	arr=[12, 18, 7, 2, 55 ,66, 4]
	print("This ar is:- ")
	printList(arr)
	mergeSort(arr)
	print("Sorted arr is:- ")
	printList(arr)