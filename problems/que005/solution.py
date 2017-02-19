class Solution(object):
    def wordBreak(self, s, wordDict):
        memo = {len(s): ['']}

        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i + 1, len(s) + 1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
                print memo

            return memo[i]

        return sentences(0)

print Solution().wordBreak("bb",["a","b","bbb","bbbb"])
print Solution().wordBreak("catsanddog",["cat","cats","and","sand","dog"])