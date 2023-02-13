import math

def is_square(n): 

    if n < 0:
        return False
    else:
        sqrt = int(math.sqrt(n))

        if sqrt * sqrt == n:
            return True
        
        else:
            return False

print(is_square(0))
