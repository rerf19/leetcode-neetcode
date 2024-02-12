class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for n in nums:
            if n in d:
                d[n] = d[n] + 1
            else:
                d[n] = 1
        
        # order d 
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)

        #prepare output
        r = []
        for i in range(k):
            r.append(d[i][0])

        return r