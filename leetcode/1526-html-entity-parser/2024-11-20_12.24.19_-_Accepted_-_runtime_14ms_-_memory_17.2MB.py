class Solution:
    def entityParser(self, text: str) -> str:
        tags = {"&quot;" : '"', "&apos;" : "'", "&gt;" : ">", "&lt;" : "<", "&frasl;" : "/",  "&amp;" : "&"}
        for i, val in tags.items():
            text = text.replace(i, val)
        return text
        
        