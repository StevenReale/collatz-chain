#initializes variables
chains = {1: 1} #this dictionary stores chain lengths for tested inputs
longest_chain = 0
longest_chain_item = 1
testMax = 1000000

#function is passed the number to test as well as the dictionary to test it on
def collatz(start_num, chain_dict):
    #if number to test is already in the dictionary, returns dictionary unchanged
    if start_num in chain_dict:
        return chain_dict

    #otherwise, determines next number to test
    elif start_num % 2 == 0:
        nextCol = start_num/2
    else:
        nextCol = 3 * start_num  + 1

    #passes next number to test into this function; checks returned dictionary for the chain length of next number on chain; adds 1 to that value and stores it as the chain length for the current number
    newVal = collatz(nextCol, chain_dict)
    chain_dict[start_num] = newVal[nextCol] + 1
    return chain_dict

#loop populates dictionary with keys from 1 to testMax
for i in range(1, testMax, 1):
    if i in chains:
        continue
    print("testing", i)
    chains = collatz(i, chains)

#loop reads dictionary to find longest chain and its associated key
for item in chains:
    if chains[item] > longest_chain:
        longest_chain=chains[item]
        longest_chain_item = item

print("The longest chain starts with", longest_chain_item, "and has", longest_chain, "terms.")
