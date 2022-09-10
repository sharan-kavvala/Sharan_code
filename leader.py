#Python is used as coding language Here.
def printLeaders(arr,size):
	
	for i in range(0, size):
		for j in range(i+1, size):
			if arr[i]<=arr[j]:
				break
		if j == size-1:
			print (arr[i],end=' ')

arr=[7, 10, 4, 10, 6, 5, 2]
printLeaders(arr, len(arr))

