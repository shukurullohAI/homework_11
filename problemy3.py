def rearrange_by_frequency(nums: list[int]) -> list[int]:
    new_dict={}
    count=0
    for num in nums:
        if num not in new_dict:
            new_dict[num]=1
        else:
            new_dict[num]+=1
    print(new_dict)   #tekshirish uchun,buni  shartga aloqasi yo'q
    replace = sorted(nums,key = lambda x: (new_dict[x], x), reverse=True)
    return replace


print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))