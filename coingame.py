# Two players, who we will call Alice and Bob, take turns removing one of the coins from either end of the remaining line 
# of coins. That is, when it is a player’s turn, he or she removes the coin at the left or right end of the line of coins 
# and adds that coin to his or her collection. The player who removes a set of coins with larger total value than the other 
# player wins, where we assume that both Alice and Bob know the value of each coin.

# coins []  =  { 6, 9, 1, 2, 16, 8}

# trial 1: (players will pick the best option available for them)
# coins [] = { 6, 9, 1, 2, 16, 8} , Alice picks 8
# coins [] = { 6, 9, 1, 2, 16}, Bob picks 16
# coins [] = { 6, 9, 1, 2}, Alice picks 6
# coins [] = { 9, 1, 2}, Bob picks 9
# coins [] = {1, 2}, Alice picks 2
# coins [] = {1}, Bob picks 1
# Alice: 8+6+2 =16 Bob: 16+9+1=26 => Alice Lost

# So clearly picking up the best in each move is not good for Alice. What else Alice can do to win the game.

# trial 2: (Alice thinks about Bob's move, Will discuss the strategy in solution) 
# coins [] = { 6, 9, 1, 2, 16, 8} , Alice picks 6
# coins [] = { 9, 1, 2, 16, 8}, Bob picks 9
# coins [] = { 1, 2, 16, 8}, Alice picks 1
# coins [] = 2, 16, 8}, Bob picks 8
# coins [] = {2, 16}, Alice picks 16
# coins [] = {2}, Bob picks 2
# Alice: 6+1+16 =23 Bob: 9+8+2=19 => Alice Won


class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        
        def pmin(i,j):
            # pmin(i, j) => Given a pile from i...j and its p2's turn to play, return what p1 will get.
            if (i,j) in mincache: return mincache[(i,j)]
            if i == j: return 0
            mincache[(i,j)] = min(pmax(i+1,j), pmax(i,j-1))
            return mincache[(i,j)]
        
        def pmax(i,j):
            # pmax(i, j) => Given a pile from i..j and its p1's turn to play, return what p1 will get.
            if (i,j) in maxcache: return maxcache[(i,j)]
            if i == j: return piles[i]
            maxcache[(i,j)] = max(piles[i]+pmin(i+1,j), pmin(i,j-1)+piles[j])
            return maxcache[(i,j)]
        mincache, maxcache = {}, {}
        p1 = pmax(0, len(piles)-1)
        p2 = sum(piles) - p1
        print p1
        return p1 > p2
