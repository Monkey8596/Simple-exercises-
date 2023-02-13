def abbrev_name(name):
    full_name = name.upper().split(' ')
    return f'{full_name[0][0]}.{full_name[1][0]}'


print(abbrev_name('sandra morales'))