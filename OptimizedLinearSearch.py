#Linear Search Optimised - from left and right side search simulaneously 
arr=[1,4,5,6,7,8,9,10,13,34,54,56,24,78,59,98]
print('Array: ',arr)
s=int(input('Enter the element to search for: '))
l=0
r=len(arr)
while l<r:
    if s==arr[l]:
        print('Element found at position: ', l+1, 'found in ', l, ' attempts' )
    if s==arr[r-1]:
        print('Element found at position: ',r, 'found in ',len(arr)-r ,' attempts')
    l+=1
    r-=1

