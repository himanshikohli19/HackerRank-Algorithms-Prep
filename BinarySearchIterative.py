#Iterative Method
def Bsearch(arr,s,left,right):
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==s:
            return mid+1
        elif arr[mid]<s:
            left=mid+1
        else:
            right=mid-1
    return -1

#Driver Code
if __name__ == '__main__':
#using already sorted array for Binary search
    arr=[2,5,7,8,9,10,12,15,17,19,23,45,56,58,67,69,70,73,76,78,79,89,98,99,102,134,156,202,214,267]
    s=7
    left=0
    right=len(arr)-1
    res=(Bsearch(arr,s,left,right))
    if res!=-1:
        print("Element is present at: ",res)
    else:
        print("Element not found")