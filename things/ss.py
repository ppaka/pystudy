def multi_num(multi, start, end):
    result = []
    for n in range(start, end):
        if n % multi == 0:
            result.append(n)
    return result

# print(multi_num(2,1,100))

def min_max(*args):
    min = args[0]
    max = args[0]
    for arg in args:
        if min > arg:
            min = arg
        if max < arg:
            max = arg
    return min,max

print(min_max(52, -3, 23, 89, -21))
min_value, max_value = min_max(52, -3, 23, 89, -21)
print("최젓값:", min_value)
print("최곳값:", max_value)