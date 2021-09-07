def digital_root(n):
    
    # Create helper function to sum all digits of a string version of an integer
    def sum_all_digits(str_n):
        
        # Find the sum of all digits
        digits_sum = 0
        for str_digit in str_n:
            digits_sum += int(str_digit)
        
        return digits_sum
    
    # Create a string version of the function parameter
    input_string = str(n)
    
    # Find the first digital root
    first_sum = sum_all_digits(input_string)
    
    # Return the first sum if the digital root is only one digit
    if len(str(first_sum)) <= 1:
        return first_sum
    
    # Keep calling the helper function until the digital root is only one digit
    else: 
        while len(input_string) > 1:
            sum_result = sum_all_digits(input_string)
            input_string = str(sum_result)
        
        return sum_result
