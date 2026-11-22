from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # num of cards must be divisible by groupsize
        if len(hand) % groupSize != 0:
            return False
        sortedHand = sorted(hand)

        # start hands from smallest numbers that cant join existing straights
        # add them to a straight if it could use it, otherwise, start a new one with it
        # if a straight is length groupsize, we can remove it and add it as a new straight

        # dict where key is the number it needs next, value is list of straights that need that number,
        # we can give it to the newest one first since all are going to need that value anyways
        straight = defaultdict(list)
        straights = 0
        for card in sortedHand:
            if card in straight:
                # pull straight out
                cur = straight[card].pop()
                # no more straights left
                if not straight[card]:
                    del straight[card]
                cur.append(card)
            # otherwise start new straight
            else:
                cur = [card]

            # enough for a straight we need, remove it
            if len(cur) == groupSize:
                straights += 1
            # otherwise it needs a new value to continue building, so move it over
            else:
                straight[card + 1].append(cur)

        return straights == (len(hand) // groupSize)
        