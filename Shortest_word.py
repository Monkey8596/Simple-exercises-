def find_short(s):
    # your code here
    return min([len(f) for f in s.split()])

print(find_short("i want to travel the world writing code one day")) 