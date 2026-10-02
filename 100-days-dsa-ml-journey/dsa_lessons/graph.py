"""
# 547

"""

def num_provinces(M):
    """
    Approach: visit from each nodes and nebs defined by having a connections with
    it , count the number of unique visits via dfs
    
    """ 
    seen = set()
    ans = 0 
    n = len(M)

    def dfs(nd):
        seen.add(nd)
        for nb in range(n):
            if M[nd][nb] == 1 and nb not in seen:
                dfs(nb)

    for nd in range(n):
        if nd not in seen:
            dfs(nd)
            ans += 1

    return ans 

from collections import deque 

def num_islands(grid):

    """
    -> iterate over all nodes to count unique visits from land '1' 
    -> return unique groups of '1' s or islands 
    
    """
    R, C = len(grid), len(grid[0])

    count = 0

    seen = set() 

    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def ok_cell(r, c):
        return 0 <= r < R and 0 <= c < C and grid[r][c] == "1"
    
    def bfs(r, c):

        q = deque([(r,c)])

        seen.add((r,c))

        while q: 

            r0, c0 = q.popleft()

            for dr, dc in dirs:
                nr, nc = r0 + dr , c0 + dc 

                if ok_cell(nr, nc) and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr,nc))

    for r in range(R):
        for c in range(C):
            if ok_cell(r,c) and (r, c) not in seen:
                bfs(r, c)
                count += 1 

    return count



test_inputs = [[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]]
expected_outputs = [1, 3]

for i, (test, exp_out) in enumerate(zip(test_inputs, expected_outputs)):
    print(f"\n===== Test {i+1} =====\nInput: {test}")
    print(f"Expected Output: {exp_out}")
    alg_out = num_islands(test)
    print(f"Algorithm Output: {alg_out}")
    if exp_out == alg_out:
        print("TEST CASE PASSED :)) ")
    else:
        print("TEST CASE FAILED ((: ")
