# Input : arr[] = {4, -10, 4, , 4}
# Output: 7

def minEnergy(arr):    
    ini_min_energy = 0
    curr_energy = 0
    energy_drop = False

    for i in range(len(arr)):
        curr_energy += arr[i]
        if curr_energy <= 0:
            ini_min_energy += abs(curr_energy) + 1
            curr_energy =1
            energy_drop = True


    # return 3
    return 1 if not energy_drop else ini_min_energy
            

    # def allPositives(arr):
    #     all_positives = True
    #     for num in arr:
    #         if num < 0:
    #             all_positives = False

    #     return all_positives

    # def allNegatives(arr):
    #     all_negatives = True
    #     for num in arr:
    #         if num > 0:
    #             all_negatives = False
                
    #     return all_negatives

    # if allPositives(arr):
    #     return 1

    # if allNegatives(arr):
    #     return abs(sum(arr)) + 1

        
print(minEnergy([4,-10,4,4,4]))
