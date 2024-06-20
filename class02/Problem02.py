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

values = [5, 8, 13, 27, 14]
print(balance_split(values))
