def subsets(nums):
    n = len(nums)
    res, sol = [], []
    
    def backtrack(i):
        if i == n:
            res.append(sol[:])#copy of solution
            return
        
        #dont pick the nums in i
        backtrack(i+1)

        #pick nums in i
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()
    
    backtrack(0)
    return res

if __name__ == "__main__":
    nums = [1, 2, 3]
    r = subsets(nums)
    print(r)