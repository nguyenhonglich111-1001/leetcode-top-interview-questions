def maxArea(height: list[int]) -> int:
    l,r = 0, height.__len__() - 1
    maxAns = 0

    while l < r:
        maxAns = max(maxAns, min(height[l], height[r])*(r-l))
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1

    return maxAns


print(maxArea([1,8,6,2,5,4,8,3,7]))