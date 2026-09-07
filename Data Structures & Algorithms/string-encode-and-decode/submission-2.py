class Solution:

    def encode(self, strs: List[str]) -> str:
        outStr = ""
        for i in strs:
            outStr += i
            outStr += " $ "
        return outStr
        

    def decode(self, s: str) -> List[str]:
        return s.split(" $ ")[:-1]