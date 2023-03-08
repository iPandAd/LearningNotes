class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        Sum = []
        m = len(accounts)
        for i in range(m):
            rst = sum(accounts[i])
            Sum.append(rst)
        maximumWealth = max(Sum)
        return maximumWealth