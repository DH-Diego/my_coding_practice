import random
def quick_select(k,array):
    # pivot_index = random.randint(start,end)
    # print(k,array)
    if len(array)<k:
        return array
    pivot = array[-1]
    left = [i for i in array[:-1] if i <= pivot] + [pivot]
    leftl = len(left)
    if leftl == k:
        return left
    elif leftl > k:
        return quick_select(k,left[:-1])
    else:
        right = [x for x in array[:-1] if x>pivot]
        return left+quick_select(k - leftl,right)

def topK(array,k):
    return (quick_select(k,array))
    # print(a)

def topKAnswerGenerator(array,k):
    array.sort()
    return array[:k]

test_case = [
    ([1,2,3,2,1,0],[1,2,3,2,1,0],3),
    ([1,4,2,13,1,351,4,1,51,24],[1,4,2,13,1,351,4,1,51,24],5),
    ([1,4,2,1,3,45,56,1,231,231,51,4,1234,12],[1,4,2,1,3,45,56,1,231,231,51,4,1234,12],10)
]

for case in test_case:
    print(topKAnswerGenerator(case[0],case[2]))
    print(topK(case[1], case[2]))
