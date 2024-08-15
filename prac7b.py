def FA(s):
    # If the length is less than 3, then it can't be accepted; therefore, end the process.
    if len(s) < 3:
        return "Rejected"
    
    # The first three characters are fixed; therefore, check them using index
    if s[0] == '1':
        if s[1] == '0':
            if s[2] == '1':
                # After index 2 only "1" can appear; therefore, break the process if any other 
                # character is detected
                for i in range(3, len(s)):
                    if s[i] != '1':
                        return "Rejected"
                return "Accepted"  # If all checks are true
            return "Rejected"  # Else for the 3rd if
        return "Rejected"  # Else for the 2nd if
    return "Rejected"  # Else for the 1st if

# Test cases
inputs = ['1', '10101', '101', '10111', '01010', '100', '', '10111101', '1011111']
for i in inputs:
    print(FA(i))
