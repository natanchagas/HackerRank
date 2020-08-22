if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
    
    for times in range(arr.count(max(arr))):
        arr.remove(max(arr))

    print(max(arr))
