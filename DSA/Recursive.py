def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0]+list_sum(num_list[1:])
print (list_sum([1,2,3,4,5,6,7,8,9,10]))    

def list_fibonacci(fib_num):
    if fib_num <= 1:
        return fib_num
    else:
        return list_fibonacci(fib_num - 1) + list_fibonacci(fib_num-2)
print (list_fibonacci(8))