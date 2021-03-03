def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    
    for query in queries: 
        a = query[0] - 1
        b = query[1]
        k = query[2]
        arr[a] += k
        arr[b] -= k
        
    max_value = 0
    running_count = 0
    for num in arr:
        running_count += num
        if running_count > max_value:
            max_value = running_count
            
    return max_value


print(
    arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])
)