def open_or_senior(data):

    result = []
    
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            result.append('Senior')
        else:
            result.append('Open')

    return result
    


print(open_or_senior([[18, 20], [45, 2],[61, 12]]))