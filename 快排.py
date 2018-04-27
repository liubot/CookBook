li = [9,22,12,1,2,3,4,5,6,7,8,26]
def quick_sort(list,start,end):
    if start < end:
        left = start
        right = end
        flag = list[left]
        while left < right:
            while left<right and list[right] > flag:
                right -= 1
            list[left]=list[right]
            while left<right and list[left] < flag:
                left += 1
            list[right]=list[left]
        list[left] = flag
        quick_sort(list,start,left-1)
        quick_sort(list,right+1,end)
        return list

res = quick_sort(li,0,len(li)-1)
print (res)