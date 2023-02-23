class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        num_lst = []
        num_str = ''
        for i in word:
            try:
                tmp = int(i)
                num_str+=i
            except:
                if num_str:
                    num_lst.append(int(num_str))
                    num_str = ''
        try:
            tmp = int(i)
            num_lst.append(int(num_str))
        except:
            pass
        return len(list(set(num_lst)))