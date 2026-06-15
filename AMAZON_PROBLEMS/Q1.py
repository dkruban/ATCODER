def compress_string(s):
    if not s: return ""
    
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    # Append the last set
    result.append(s[-1] + str(count))
    return "".join(result)

def decompress_string(compressed):
    result = []
    i = 0
    while i < len(compressed):
        char = compressed[i]
        i += 1
        num_str = ""
        # Extract full number if > 9
        while i < len(compressed) and compressed[i].isdigit():
            num_str += compressed[i]
            i += 1
        
        if not num_str: 
            num_str = "1" # Should not happen based on format, but safe fallback
            
        count = int(num_str)
        result.append(char * count)
    return "".join(result)

# Example Usage
# print(compress_string("AAACCCBBD")) -> A3C3B2D
# print(decompress_string("A3C3B2D")) -> AAACCCBBD
