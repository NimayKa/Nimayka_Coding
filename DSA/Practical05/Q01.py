def InsertionSort(List):
    for i in range(1, len(List)):
        key = List[i]
        j = i-1
        while j >=0 and key < List[j]:
            List[j+1] = List[j]
            j -= 1
        List[j+1] = key
    return List

TestList = [54, 26, 93, 17, 20]
print("List:", TestList)
print("InsertionSort(TestList)")
print("Result:", InsertionSort(TestList))