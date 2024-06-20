def balance_split(values):
    n = len(values)
    
    def recursive_split(index, group1_sum, group2_sum):
        if index == n:
            return abs(group1_sum - group2_sum)
        
        include_in_group1 = recursive_split(index + 1, group1_sum + values[index], group2_sum)
        include_in_group2 = recursive_split(index + 1, group1_sum, group2_sum + values[index])

        return min(include_in_group1, include_in_group2)
    
    min_difference = recursive_split(0, 0, 0)
    return min_difference

with open('class02/balanceNum/5.in', 'r') as file:
    content = file.read().strip()
    values = list(map(int, content.split()))


print(balance_split(values))


# 01 ANS: 44790
# 02 ANS: 30
# 03 ANS: 603
# 04 ANS: 70
# 05 ANS: 459

