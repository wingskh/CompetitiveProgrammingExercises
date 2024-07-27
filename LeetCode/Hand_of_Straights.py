# https://leetcode.com/problems/hand-of-straights/\
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        elif groupSize == 1:
            return True
        
        hand.sort()
        total_card_size = len(hand)
        for i in range(total_card_size):
            if hand[i] != -1:
                acc_size = 1
                for j in range(i + 1, total_card_size):
                    if hand[i] + acc_size == hand[j]:
                        acc_size += 1
                        hand[j] = -1

                    if acc_size == groupSize:
                        break
                
                if acc_size != groupSize:
                    return False
                hand[i] = -1

        return True if all(card == -1 for card in hand) else False


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
# Output = True
# hand = [8, 10, 12]
# groupSize = 3
# Output = false
# hand = [1,2,3]
# groupSize = 1
# Output = True
sol = Solution()
print(sol.isNStraightHand(hand, groupSize))
