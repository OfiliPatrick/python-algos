# def buyAndSell2(prices):
#     min_cp = float('inf')
#     max_profit = 0

#     for day in range(len(prices)):
#         price = prices[day]

#         min_cp = min(min_cp, price)

#         profit = price - min_cp

#         max_profit = max(max_profit, profit)
        

#     return max_profit


# print(buyAndSell2([7, 1, 5, 3, 6, 4]))
# print(buyAndSell2([7, 6,4,3,1]))

def longestCommonPrefix(strs):
        
    if strs == []:
        return ''

    if len(strs) == 1:
        return strs[0]

    curr_pref = strs[0]
    pref_length = len(curr_pref)

    for string in strs[1:]:
         
        while curr_pref != string[0:pref_length]:

            pref_length -= 1
            curr_pref = curr_pref[0: (pref_length)]
            print(curr_pref)
            if pref_length == 0:
                return 0

    return curr_pref
            
            
print(longestCommonPrefix(['flower', 'flow', 'flight']))