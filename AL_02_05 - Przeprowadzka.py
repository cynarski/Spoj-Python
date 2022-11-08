t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    values.sort()
    boxes = 0
    left, right = 0, n - 1
    while left <= right:
        boxes += 1
        if values[left] + values[right] <= k:
            left += 1
            right -= 1
        else:
            right -= 1
    print(boxes)