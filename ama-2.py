def binsearch(arr, key, s, e):
    mid = int(s+((e-s)/2))
    if(s>e):
        return -1
    if(arr[mid] == key):
        print("==",mid)
        return mid
    elif(arr[mid] > key):
        print("called >",s,mid)
        binsearch(arr,key, s, mid)
    elif(arr[mid] < key):
        print("called <",mid+1,e)
        binsearch(arr,key, mid+1, e)
if __name__ == '__main__':
    arr = [3,8,9,11,14,16,18,21,36,74]
    key = 9
    f = binsearch(arr,key, 0, len(arr)-1)
    print(f)