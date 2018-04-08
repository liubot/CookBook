li = [11,22,3,4,1,2,8,9,19,18]

def quick_sort(list,start,end):
    if start < end:
        left  = start
        right = end
        flag = list[start]
        while left < right:
            while left < right and list[right] > flag:
                right -= 1
            list[left] = list[right]
            while left < right and list[left] < flag:
                left += 1
            list[right] = list[left]
        list[left] = flag
        quick_sort(list,start,left-1)
        quick_sort(list,right+1,end)
        return list

def maopao(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

# print (quick_sort(li,0,len(li)-1)
print (maopao(li))