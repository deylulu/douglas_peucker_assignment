def read_points(filename):
    points = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) == 2:
                x = float(parts[0])
                y = float(parts[1])
                points.append((x, y))

    return points


def perpendicular_distance(point, start, end):
    x0, y0 = point
    x1, y1 = start
    x2, y2 = end

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5

    numerator = abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1)
    denominator = (dx ** 2 + dy ** 2) ** 0.5

    return numerator / denominator


def douglas_peucker(points, epsilon):
    if len(points) <= 2:
        return points

    start = points[0]
    end = points[-1]

    max_distance = 0
    index = 0

    for i in range(1, len(points) - 1):
        distance = perpendicular_distance(points[i], start, end)

        if distance > max_distance:
            max_distance = distance
            index = i

    if max_distance > epsilon:
        left_part = douglas_peucker(points[:index + 1], epsilon)
        right_part = douglas_peucker(points[index:], epsilon)

        return left_part[:-1] + right_part
    else:
        return [start, end]


def write_points(filename, points):
    with open(filename, "w") as file:
        for x, y in points:
            file.write(str(x) + " " + str(y) + "\n")