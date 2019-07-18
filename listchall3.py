list1 = [5, 3, 7, 1, 8]
largenum=0
product = 1

for i in list1:
    #if(list1[i]>list1[i+1]):
        #largenum = list1[i]
    if(largenum<i):
        largenum = i

print(largenum)

for num in list1:
    product*= num
    print(product)

list1.append(2)
list1.append(4)
list1.append(6)
list1.append(9)


list2 = (sorted(list1, reverse = True))
print(list2)
newlist = []
for i in list2:
    if not (i%2==0):
        list1[i::]
        print(list2)
