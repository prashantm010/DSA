class Solution:
    def numTrees(self, N):
        # Initialize the DP table with base cases
        dp = [0] * (N + 1)
        dp[0] = 1  # One way to arrange 0 nodes (empty tree)
        dp[1] = 1  # One way to arrange 1 node
        
        # Fill the DP table for all values from 2 to N
        for i in range(2, N + 1):
            for j in range(1, i + 1):
                dp[i] = (dp[i] + dp[j - 1] * dp[i - j]) % 1000000007
        
        # Return the result for N nodes
        return dp[N]

# Main function to test the code
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()
    
    # Example input
    N = 3  # Number of nodes
    result = solution.numTrees(N)
    
    # Output the result
    print(f"The number of unique BSTs that can be formed with {N} nodes is: {result}")
