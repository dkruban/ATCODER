class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters = []
        digits = []
        
        for x in logs:
            # Just look at the first character after the space
            # to see if it's a digit or letter
            first_space = x.index(" ")
            if x[first_space + 1].isdigit():
                digits.append(x)
            else:
                letters.append(x)
                
        # A quick custom sort for the letters
        def my_sort(log):
            space = log.index(" ")
            identifier = log[:space]
            content = log[space+1:]
            return (content, identifier)
            
        letters.sort(key=my_sort)
        
        return letters + digits
