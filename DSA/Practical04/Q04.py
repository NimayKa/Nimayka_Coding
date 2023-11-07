def RangeSearch(List, a, b):
    Result = []
    for i in List:
        if i >= a and i <= b:
            Result.append(i)
    if not Result:
        return "No result found"
    else:
        return Result

TestList = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print("List:", TestList)
print("RangeSearch(TestList, 2, 12)")
print("Range search result:", RangeSearch(TestList, 2, 12))
print("RangeSearch(TestList, 20, 25)")
print("Range search result:", RangeSearch(TestList, 20, 25))