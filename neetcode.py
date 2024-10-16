li=[1,1,2,3,3,3,2]
count={}
for i in li:
    count[i]=1+count.get(i,0)
print(count)