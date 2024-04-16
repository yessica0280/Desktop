def sumas(nums, target):
    numer_dic = {}
    for i, num in enumerate(nums):
        complement = target - num

        if complement in numer_dic:
            return[numer_dic[complement], i]
        numer_dic[num] = i 
    return "No se encontraron dos nùmeros que sumen el objetivo"
   
numeros = input()
nums_strings = numeros.split()
nums=[int(nums_str) for nums_str in nums_strings]
target = int(input())
result = sumas(nums, target)
print(f"{result}")
