class Solution:
    def entityParser(self, text: str) -> str:
        tags = {"&quot;":'"', "&apos;":"'", "&amp;":"&", "&gt;":">", "&lt;":"<", "&frasl;":"/"}
        for i, val in tags.items():
            text = text.replace(i, val)
        return text
        
        