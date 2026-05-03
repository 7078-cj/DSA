
def lengthOfSubstring(word):
    l=0
    longest = 0
    sett = set()
    n=len(word)
    
    for r in range(n):
        while word[r] in sett:
            sett.remove(word[l])
            l += 1

        w = (r - l ) + 1
        longest = max(longest, w)
        sett.add(word[r])
    
    return longest

def maxAverage(nums,k):
    
    n = len(nums)
    cur_sum = 0
    
    for i in range(k):
        cur_sum += nums[i]
        
    max_avg = cur_sum / k
    
    for i in range(k, n):
        cur_sum += nums[i]
        cur_sum -= nums[i-k]
        
        avg = cur_sum / k
        max_avg = max(max_avg, avg)
        
    return max_avg
    
if __name__ == '__main__':
    word = 'abcabcbb'
    nums = [1, 12, -5, -6, 50, 3]
    
    l = lengthOfSubstring(word)
    print(l)
    print()
    m = maxAverage(nums, 4)
    print(m)