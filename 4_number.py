def func(nums):
    two_number_sum_result_dict = {}
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i]+nums[j]) not in two_number_sum_result_dict:
                two_number_sum_result_dict[nums[i]+nums[j]] = [[i,j]]
            elif ([nums[i],nums[j]] not in two_number_sum_result_dict[nums[i]+nums[j]]) and ([nums[j],nums[i]] not in two_number_sum_result_dict[nums[i]+nums[j]]):
                two_number_sum_result_dict[nums[i]+nums[j]].append([i,j])
    #print(two_number_sum_result_dict)
    return two_number_sum_result_dict

def func3(nums,target):
    two_number_sum_result_dict = func(nums)
    add_numbers = []
    result = []
    myresult = []
    if len(two_number_sum_result_dict) >1:
        for i,j in two_number_sum_result_dict.items():
            add_numbers.append(i)
    elif len(two_number_sum_result_dict) == 1:
        for i, j in two_number_sum_result_dict.items():
            add_numbers.append(i)
            add_numbers.append(i)
    #print(add_numbers)
    for i in range(len(add_numbers)):
        for j in range(i+1,len(add_numbers)):
            if (add_numbers[i]+add_numbers[j]) == target:
                result += func2(two_number_sum_result_dict[add_numbers[i]],two_number_sum_result_dict[add_numbers[j]])#两个数组内的元素排列组合
    result = func4(result)
    for i in result:
        temp = []
        for j in i:
            temp.append(nums[j])
        if sorted(temp) not in myresult:
            myresult.append(sorted(temp))
    return myresult

def func2(list1,list2):
    result = []
    for i in list1:
        for j in list2:
            result.append(i+j)
    return result

def func4(result):
    sorted_list = []
    set_list = []
    for i in result:
        temp = sorted(i)
        if temp not in sorted_list:
            sorted_list.append(temp)
    for i in sorted_list:
        temp = set(i)
        if len(temp) == 4:
            set_list.append(list(temp))
    return set_list
print(func3([1,4,-3,0,0,0,5,0],0))
