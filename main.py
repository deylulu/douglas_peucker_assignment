from dp import read_points, douglas_peucker, write_points

input_file = "line.txt"
output_file = "output.txt"
epsilon = 0.1

points = read_points(input_file)
result = douglas_peucker(points, epsilon)

write_points(output_file, result)

print("Original points:", len(points))
print("Simplified points:", len(result))
print("Result:")

for point in result:
    print(point)