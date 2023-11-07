def BubbleSort(List):
    n = len(List)
    for i in range(n):
        for j in range(0, n-i-1):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
                print("Exchange")
            else:
                print("No Exchange")
    return List

def BubbleSortWithIterations(List):
    n = len(List)
    for i in range(n):
        is_sorted = True
        for j in range(0, n-i-1):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
                is_sorted = False
        if is_sorted:
            break
        print("Iteration", i+1, ":", "Exchange" if not is_sorted else "No Exchange")
    return List

TestList = [54, 93, 17, 20]
print("List:", TestList)
print("BubbleSort (TestList)")
print("Result:", BubbleSort(TestList))
print("BubbleSortWithIterations(TestList)")
print("Result:", BubbleSortWithIterations(TestList))