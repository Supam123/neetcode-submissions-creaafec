class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        counts = {}
        for h in hand:
            counts[h] = counts.get(h,0) + 1
        '''
        {1: 1, 2: 2, 3: 2, 4: 2, 5: 1}
        '''
        
        for card in sorted(counts):
            if counts[card] == 0:
                continue
                
            need =  counts[card]
            for nextCard in range(card,card+groupSize):
                if nextCard in counts and counts[nextCard] > 0:
                    print(counts)
                    counts[nextCard] -= need
                else:
                    return False
        return True