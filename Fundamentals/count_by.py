def count_by(x,n):
    result = []

    # for numbers in range(1, n + 1):
    #     result.append(numbers * x)

    return [x*i for i in range(1,n+1)]

print(count_by(2,5))


