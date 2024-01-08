def quicksort(array: list) -> list:
    if len(array) > 1:
        num = array[0]        
        great = [x for x in array if x > num]
        same = [x for x in array if x == num]
        low = [x for x in array if x < num]
        result = quicksort(low) + same + quicksort(great)
        return result
    return array


def bubble_sort(array: list):    
    num = 1
    flag=True
    while flag:
        flag = False
        for i in range(len(array) - num):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag = True                
        num += 1
    return array

a = [1,2,3,4,6,6,2,1,123,4,5,1,3,213,123,125,13,4356,4576,54672,341,234,21,3421,52,3423421,412,-2]

b = quicksort(a)
print(b)
c =bubble_sort(a)
print(c)





