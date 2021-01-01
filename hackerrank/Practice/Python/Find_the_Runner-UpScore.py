if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr.sort()
    arr = list(arr)
    arr1 = []
    for i in range(len(arr)):
        if arr[i] < max(arr):
            arr1.append(arr[i])

    print(arr1[-1])



