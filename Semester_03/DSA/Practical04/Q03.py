def BinarySearch(List, SearchValue):
    Low = 0
    High = len(List) - 1

    while Low <= High:
        Mid = (Low + High) // 2
        if List[Mid] == SearchValue:
            return Mid
        elif List[Mid] < SearchValue:
            Low = Mid + 1
        else:
            High = Mid - 1

    return -1

TestList = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print("List:", TestList)
print("BinarySearch(TestList, 37)")

Result = BinarySearch(TestList, 37)

if Result != -1:
    print("37 is found at index", Result)
else:
    print("37 is not found")