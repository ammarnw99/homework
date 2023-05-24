list1 = ['http','https','ftp','dns']
list2 = [80,443,20,53]
d = {k:v for (k,v) in zip(list1,list2)}
print(d)