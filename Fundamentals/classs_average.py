import statistics

def better_than_average(class_points, your_points):
    # Your code here
    return statistics.mean(class_points) < your_points

print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))
