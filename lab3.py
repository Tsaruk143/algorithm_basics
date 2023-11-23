from PIL import Image, ImageDraw
from functools import cmp_to_key

p0 = None

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def distance(p, q):
    return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])

def compare(p1, p2):
    o = orientation(p0, p1, p2)
    if o == 0:
        if distance(p0, p2) >= distance(p0, p1):
            return -1
        else:
            return 1
    else:
        if o == 2:
            return -1
        else:
            return 1

def convexHull(points, n):
    min_y = float('inf')
    min_index = -1

    for i in range(n):
        if points[i][1] < min_y or (points[i][1] == min_y and points[i][0] < points[min_index][0]):
            min_y = points[i][1]
            min_index = i

    global p0
    points[0], points[min_index] = points[min_index], points[0]
    p0 = points[0]

    points = sorted(points, key=cmp_to_key(compare))

    m = 1
    for i in range(1, n):
        while i < n-1 and orientation(p0, points[i], points[i+1]) == 0:
            i += 1
        points[m] = points[i]
        m += 1

    if m < 3:
        return

    S = []
    S.append(points[0])
    S.append(points[1])
    S.append(points[2])

    for i in range(3, m):
        while len(S) >= 2 and orientation(S[-2], S[-1], points[i]) != 2:
            S.pop()
        S.append(points[i])

    return S

def read_dataset(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            y, x = map(int, line.strip().split())
            data.append((x, y))
    return data

def draw_convex_hull(points, hull, image_width, image_height):
    image = Image.new('RGB', (image_width, image_height), 'white')
    draw = ImageDraw.Draw(image)

    for i in range(1, len(hull) + 1):
        if i == len(hull):
            i = 0
        p1 = hull[i-1]
        p2 = hull[i]
        draw.line([p1, p2], fill='black')

    for point in points:
        draw.point(point, fill='red')

    image.save('DS9_lab3.png')
    image.show()

image_width = 960
image_height = 540

dataset_file = 'DS9.txt'
data = read_dataset(dataset_file)

hull = convexHull(data, len(data))
draw_convex_hull(data, hull, image_width, image_height)
