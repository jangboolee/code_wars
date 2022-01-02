def tribonacci(signature, n):
    
    if n == 0:
        return []
    elif n < 3:
        return signature[:n]
    else:
        tribonacci = signature
        i = 0
        while n > 3:
            tribonacci.append(sum(tribonacci[i:i+3]))
            i += 1
            n -= 1
        return tribonacci
