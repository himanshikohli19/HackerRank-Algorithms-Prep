#BINARY SEARCH
#Iterative Approach
arr= [2,3,4,6,8,9,10,15,19,23,27,29,55,57,59,70,91]
print(arr)
s=int(input("Enter the element to search for: "))
l=0
r=len(arr)-1
mid=0
while l<=r:
    mid=(r+l)//2
    if arr[mid]<s:
        l=mid+1
    elif arr[mid]>s:
        r=mid-1
    elif arr[mid]==s:
        print(' Element found at:', mid+1)
        break
    else:
        print("Element not found!")
