reviews = ["rugved is", "sure why?", "cup is here", "cup is not here", "rugved oractuve", "rugved opop", "rugved iukt", "cup lokit", "amazon ", "amazon", "amazon", "sonu", "sonu ", "sonu", "worldCup"]
companies = ["rugved", "sure", "cup", "sonu", "amazon"]
topComps = int(input("Enter the number of companies"))
compDict = dict(map(lambda x: (x, 0), companies))

for i in reviews:
     for j in companies:
         if(j in i.lower()):
            compDict[j] +=1
listCon = {k: v for k, v in sorted(compDict.items(), key=lambda item: item[1])}
print(list(listCon.keys())[0:3])

'''
print items who's indices are even
filter(lambda (i,x): (i%2!=0), enumerate(a))
a[0::1] start from 0, till the end and skip 1 value in the list

sort by value
sorted(compDict.items(), key=lambda item: item[1])  returns a list of tuples 
 {k: v for k, v in sorted(compDict.items(), key=lambda item: item[1])} creates an dict from it
 
'''