def characterReplacement(s: str, k: int) -> int:
    count = {}
    
    length = 0
    l = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        while (r-l+1) -max(count.values()) > k:
            count[s[l]] -=1
            l+=1

        length = max(length, r-l+1)
    
    return length

def maxValue(s: str, k: int) -> int:
    count = {}
    
    maxValue = 0
    length = 0
    l = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        maxValue = max(maxValue, count[s[r]])

        while (r-l+1) - maxValue > k:
            count[s[l]] -=1
            l+=1

        length = max(length, r-l+1)
    
    return length