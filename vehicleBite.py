import pandas as pd

class vehicleBite:
    def load(self):
        df = pd.read_csv("Scrap.csv",encoding = 'utf8')
        return df
    def insertionSort(self,array,index,type):

        for j in range(1,len(array)):
        
            key = array[j]
            i = j-1
        #     print(array[j])
            
            if(type == "Ascending"):
                
                while i>-1 and str(array[i][index]) > str(key[index]):
                
                    array[i+1] = array[i]
                    i = i-1 
                #     print(array[i])

            else:
                while i>-1 and str(array[i][index]) < str(key[index]):
                        
                    array[i+1] = array[i]
                    i = i-1 

            array[i+1]= key
        return array
    def selectionSort(self,array,index,type):
        size = len(array)

        for j in range(size):
            min = j
            if(type == "Ascending"):
                for i in range(j + 1, size):
                
                    if str(array[i][index]) < str(array[min][index]):
                        min = i
            else:
                for i in range(j + 1, size):
                
                    if str(array[i][index]) > str(array[min][index]):
                        min = i
         
            array[j], array[min] = array[min], array[j]

        return array
    def merge(self,arr, l, m, r,index):
	    n1 = m - l + 1
	    n2 = r - m

	    L = [0] * (n1)
	    R = [0] * (n2)

	    for i in range(0, n1):
	    	L[i] = arr[l + i]

	    for j in range(0, n2):
	    	R[j] = arr[m + 1 + j]

	    i = 0	
	    j = 0	
	    k = l	 
	    while i < n1 and j < n2:
	    	if str(L[i][index]) <= str(R[j][index]):
	    		arr[k] = L[i]
	    		i += 1
	    	else:
	    		arr[k] = R[j]
	    		j += 1
	    	k += 1
	    while i < n1:
	    	arr[k] = L[i]
	    	i += 1
	    	k += 1
	    while j < n2:
	    	arr[k] = R[j]
	    	j += 1
	    	k += 1

    def mergeSort(self,arr, l, r,index):
    	if l < r:
    		m = l+(r-l)//2
    		self.mergeSort(arr, l, m,index)
    		self.mergeSort(arr, m+1, r,index)
    		self.merge(arr, l, m, r,index)



