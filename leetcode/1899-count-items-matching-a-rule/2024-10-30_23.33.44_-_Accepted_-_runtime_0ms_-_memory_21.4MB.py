class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        target = 0
        if ruleKey == "type": target = 0
        if ruleKey == "color": target = 1
        if ruleKey == "name": target = 2

        count = 0
        for i in range(len(items)):
            if items[i][target] == ruleValue:
                count += 1

        return count
        