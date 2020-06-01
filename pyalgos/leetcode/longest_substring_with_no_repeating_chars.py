# The answer to the problem is weird because they're not asking for the substring
# itself, just its length.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        end = 0
        longest = 0
        substr_start = 0
        while start < len(s) and end < len(s):
            char = s[end]
            if char not in seen:
                seen.add(char)
                end += 1
                if len(seen) > longest:
                    substr_start = start
                    longest = len(seen)

            else:
                while True:
                    to_remove = s[start]
                    seen.remove(to_remove)
                    start += 1
                    if to_remove == char:
                        break

        print("Longest is '{}' with length {}".format(
            s[substr_start:substr_start+longest],
            longest)
        )
        return longest
