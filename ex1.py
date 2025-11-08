def find(s, n):
# write your implementation here
     for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i]+s[j]==n:
                return [i,j]
            
    
