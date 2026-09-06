from collections import Counter 


def num_jewels_in_stones(jewels, stones):
    jewels_counter = Counter(jewels)
    stones_counter = Counter(stones)

    jewels_in_stones_count = 0

    for (k, v) in stones_counter.items():
        if k in jewels_counter:
            jewels_in_stones_count += v
    return jewels_in_stones_count



tests = [("aA","aAAbbbb"), ("z", "ZZ")] 
exp_outs = [3, 1]

for i, (test, exp_out) in enumerate(zip(tests, exp_outs)):
    alg_out = num_jewels_in_stones(*test)
    if alg_out == exp_out:
        print(f" \n --------------- test case {i+1} ------ PASSED 👏 !!! -------  \n \t Input = {test} , \n \t Expected Output = {exp_out}, \n \t Algorithm Output = {alg_out}")
    else:
        print(f" \n --------------- test case {i+1} ------ FAILED 😔 !------  \n \t Input = {test} , \n \t Expected Output = {exp_out}, \n \t Algorithm Output = {alg_out}")
        