def perm(s):
    output = []
    seen = {}
  
    def helper(choices, chosen):

        if len(choices) == len(chosen):
            output.append(chosen)

        else:

            for i in range(len(choices)):
                #choose
                if seen.get(i, False) == False:
                    chosen += choices[i]
                    seen[i] = True                

                    #explore other choices
                    helper(choices, chosen)


                    #unchoose
                    seen[i] = False
                    chosen = chosen[:len(chosen)-1]

        
    helper('abc', "")
    return output

print(perm('abc'))

            