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

    # return n > -1 and math.sqrt(n) % 1 == 0;

print(is_square(4))
