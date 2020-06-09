import statistics as s

def mergeSort(array):
	if(len(array) >1):
		mid = len(array)//2
		
		L = array[:mid]
		R = array[mid:]

		mergeSort(L)
		mergeSort(R)

		#merge L and R
		i=j=k=0
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				array[k] = L[i]
				i += 1
			else:
				array[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			array[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			array[k] = R[j]
			j += 1
			k += 1
	
l = [0.733,   	0.862,   	0.868,   	0.910,   	0.921,   	0.931,   	0.980,   	1.009,   
1.039,   	1.048,   	1.092 ,  	1.119  , 	1.130,   	1.156,   	1.231,   	1.039] #-0.43
mergeSort(l)
#print("post sort %s" %l)
print("median " + str(s.median(l)))
#print("mean " + str(s.mean(l)))
#print("std deviation " + str(s.pstdev(l)))
#print("variance " + str(s.variance(l)))
