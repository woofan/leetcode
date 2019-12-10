def combinationSum(candidates,target):
    list_len = len(candidates)
    if list_len == 0:
        return []
    candidates.sort()
    result = []
    def helper(i,tmp,target):
        if target == 0:
            result.append(tmp)
            return
        if i == list_len or target < candidates[i]:
            return
        helper(i,tmp+[candidates[i]],target-candidates[i])
        helper(i+1,tmp,target)
    helper(0,[],target)
    return result

print(combinationSum([2,3,6,7],7))


