arr = [4, 5, 6, 2, 3, 4]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == 9:
            print(arr[i], arr[j])