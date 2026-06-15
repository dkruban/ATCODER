class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters = []
        digits = []
        for x in logs:
            first_space = x.index(" ")
            if x[first_space + 1].isdigit():
                digits.append(x)
            else:
                letters.append(x)
        def my_sort(log):
            space = log.index(" ")
            identifier = log[:space]
            content = log[space+1:]
            return (content, identifier)
            
        letters.sort(key=my_sort)
        
        return letters + digits
