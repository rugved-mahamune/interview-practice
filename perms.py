def populate(pos,curr,result):
    if(pos == len(nums)):
        result.append(curr)
        return
    for i in mapping[nums[pos]]:
        print(curr)
        populate(pos+1,curr + i,result)

nums = [3,5,2]
mapping = {0:'-1', 1:'-1', 2: 'abc', 3: 'def', 4:'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
output = []
currM = ['']
populate(0,"",output)
print(output)


