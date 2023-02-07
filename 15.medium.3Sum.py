# NOTE 308 / 312 testcases passed - Time Limit Exceeded
def threeSum(self, nums: list[int]) -> list[list[int]]:
    lenNums = nums.__len__()

    triplet = []

    for i in range(lenNums-2):
        for j in range(i+1, lenNums-1):
            for k in range(j+1, lenNums):
                if nums[i] + nums[j] + nums[k] == 0:
                    tmpAns = [nums[i],nums[j],nums[k]]
                    tmpAns.sort()
                    if tmpAns in triplet:
                        continue
                    triplet.append(tmpAns)

    return triplet

# NOTE 290 / 312 testcases passed - Time Limit Exceeded
def threeSum(self, nums: list[int]) -> list[list[int]]:
    lenNums = nums.__len__()

    triplet = []

    doubleNums = []
    counter = {}

    for num in nums:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1

    for i in range(lenNums-1):
        for j in range(i+1, lenNums):
            doubleNums.append({
                'sum' : nums[i] + nums[j],
                'element' : [nums[i],nums[j]]
            })

    for i in range(lenNums):
        for j in range(doubleNums.__len__()):

            if (nums[i] not in doubleNums[j]['element']):
                if nums[i] + doubleNums[j]['sum'] == 0:
                    tmpAns = [nums[i],*doubleNums[j]['element']]
                    tmpAns.sort()

                    if tmpAns in triplet:
                        continue
                    triplet.append(tmpAns)
            elif (doubleNums[j]['element'].count(nums[i]) - counter[nums[i]] != 0):
                if nums[i] + doubleNums[j]['sum'] == 0:
                    tmpAns = [nums[i],*doubleNums[j]['element']]
                    tmpAns.sort()

                    if tmpAns in triplet:
                        continue
                    triplet.append(tmpAns)

           
        
    return triplet
    
# NOTE 311 / 312 testcases passed - Time Limit Exceeded
def threeSum(self, nums: list[int]) -> list[list[int]]:

    triplet = []

    doubleNums = []
    counter = {}

    for num in nums:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1

    nums = []
    if counter.get(0,0) != 0:
        count0 = 3 if counter[0] >= 3 else counter[0]
        nums = [0]*count0

    for num, count in counter.items():
        countNum = 2 if count >= 2 else 1
        nums += [num]*countNum


    print(nums)
    lenNums = nums.__len__()
    for i in range(lenNums-1):
        for j in range(i+1, lenNums):
            sum = nums[i] + nums[j]
            element = [nums[i],nums[j]]
            opposite = 0 - sum
            
            if counter.get(opposite, 0) > 0:
                if counter[opposite] - element.count(opposite) >= 1:
                    tmpAns = element + [opposite]
                    tmpAns.sort()

                    if tmpAns not in triplet:
                        triplet.append(tmpAns)
                

        
    return triplet

# NOTE Beats 37.70%
def threeSum(self, nums: list[int]) -> list[list[int]]:

    triplet = []

    doubleNums = []
    counter = {}

    for num in nums:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1

    nums = []
    if counter.get(0,0) != 0:
        count0 = 3 if counter[0] >= 3 else counter[0]
        nums = [0]*count0

    for num, count in counter.items():
        countNum = 2 if count >= 2 else 1
        nums += [num]*countNum


    print(nums)
    lenNums = nums.__len__()
    tripletHash = {}
    for i in range(lenNums-1):
        for j in range(i+1, lenNums):
            sum = nums[i] + nums[j]
            element = [nums[i],nums[j]]
            opposite = 0 - sum
            
            if counter.get(opposite, 0) > 0:
                if counter[opposite] - element.count(opposite) >= 1:
                    tmpAns = element + [opposite]
                    tmpAns.sort()
                    tmpAnsStr = tmpAns.__str__()
                    if tmpAnsStr not in tripletHash:
                        tripletHash[tmpAnsStr] = True
                        triplet.append(tmpAns)
                

        
    return triplet

# NOTE Beats 66.15%
def threeSum(self, nums: list[int]) -> list[list[int]]:

    nums.sort()
    triplets = []
    for i in range(len(nums)-2):

        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]

        l,r = i+1, len(nums)-1

        while l < r:

            doubleSum = nums[l] + nums[r]
            if target < doubleSum:
                r -= 1
            elif target > doubleSum:
                l += 1
            else:
                triplets.append([nums[i],nums[l],nums[r]])

                while l < r and nums[l] == nums[l+1]: l += 1
                while l < r and nums[r-1] == nums[r]: r -= 1
                l += 1
                r -= 1

    return triplets