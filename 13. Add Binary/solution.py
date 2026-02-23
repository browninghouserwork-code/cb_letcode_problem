def add_binary(a: str, b: str) -> str:
    result = []
    # Set pointers to the last index of each binary string
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    # Continue looping while there are digits left in either string or a carry remains
    while i >= 0 or j >= 0 or carry:
        # Read the current digit from string a if available, otherwise treat it as 0
        if i >= 0: digit_a = int(a[i])
        else: digit_a = 0
        if j >= 0: digit_b = int(b[j])  
        else: digit_b = 0         
        
        total = digit_a + digit_b + carry # Calculate the total of the current digits plus the carry
        
        result.append(str(total % 2)) # Append the current binary digit (total modulo 2) to the result
        
        carry = total // 2
        # Move both pointers one step to the left
        i -= 1
        j -= 1
    
    return ''.join(reversed(result))
