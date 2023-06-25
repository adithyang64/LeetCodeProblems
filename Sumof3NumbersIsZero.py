
arr1 = [1,3,4,-3,-1]
for i in range(len(arr1)):
  for j in range(i+1,len(arr1)):
    for k in range(j+1,len(arr1)):
      if(arr1[i]+arr1[j]+arr1[k]==0):
        print(arr1[i],arr1[j],arr1[k])

