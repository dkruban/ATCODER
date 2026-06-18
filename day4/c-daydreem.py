import sys

def solve():
    # Read the input string
    s = sys.stdin.read().strip()
    
    # Define the allowed words
    words = ["dream", "dreamer", "erase", "eraser"]
    
    # Process from the end of the string to the beginning
    while s:
        matched = False
        for word in words:
            # Check if the string ends with the current word
            if s.endswith(word):
                # Remove the word from the end
                s = s[:-len(word)]
                matched = True
                break
        
        # If none of the words matched the end, it's impossible
        if not matched:
            print("NO")
            return
            
    # If the string becomes completely empty, a match is found
    print("YES")

if __name__ == '__main__':
    solve()
