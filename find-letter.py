def linearsearch(arr, v):
       for i in range(len(arr)):
           if arr[i] == v:
               return i
       
arr = ["Jireh","Sarah", "Michaela" ,"Mina"]
v = "Sarah"
print("Name found at index "+str(linearsearch(arr,v)))