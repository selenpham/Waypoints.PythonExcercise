# Waypoint 8: Calculate Distance between several 2D Points
# Write a function calculate_euclidean_distance_between_points that takes an arguments points, representing a list of points in a two-dimensional Cartesian coordinate system, and that returns the sum of the Euclidean distance between each consecutive points in this list.
# Each point in the list is represented with a named tuple of 2 integers or floats (x, y) where x corresponds to the position of the point on the X-axe (i.e, abscissa), and y corresponds to the position of the point on the Y-axe (i.e., ordinate).
# The function raises an exception ValueError if the given list contains less than 2 points.
# For examples:
# >>> calculate_euclidean_distance_between_points([(0, 0), (3, 4)])
# 5.0
# >>> calculate_euclidean_distance_between_points([(0, 0), (3, 4), (0, 0)])
# 10.0
# >>> calculate_euclidean_distance_between_points([(0, 0), (3, 4), (-1, -1)])
# 11.403124237432849
# >>> calculate_euclidean_distance_between_points([])

import math

#B1: tạo hàm tính khoảng cách giữa các điểm 
def calculate_euclidean_distance_between_points(points):
# Tạo ràng buộc nhập ít nhất 2 điểm
    if len(points) < 2:
        raise ValueError("The list MUST contain at least 2 points")

# Tạo list tính toán khoảng cách giữ các điểm
    distances = [calculate_euclidean_distance_between_2_points(points[i], points[i+1]) for i in range(len(points)-1)]
    
# Trả về tổng khoảng cách Euclidean 
    return sum(distances)

#Tạo hàm tính khoảng cách giữa 2 điểm
def calculate_euclidean_distance_between_2_points(p1, p2):
# Sử dụng định lý pytago
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

# Tạo hàm input các điểm
def get_coordinates(n):
# Yêu cầu người dùng nhập tọa độ cho n điểm
    print("Enter the coordinates for {} points:".format(n))
    points = []
    for i in range(n):
        while True:
            try:
                x = float(input("Enter the x-coordinate for point {}: ".format(i+1)))
                y = float(input("Enter the y-coordinate for point {}: ".format(i+1)))
                points.append((x, y))
                break
            except ValueError:
                print("Invalid input, please enter a number for the coordinates.")

# tạo ràng buộc nếu nhập ít hơn 2 điểm
    if len(points) < 2:
        raise ValueError("The list MUST contain at least 2 points")

    return points

try:
    while True:
        try:
            n = int(input("Enter the number of points (must be >= 2): "))
            if n < 2:
                raise ValueError("Number of points must be at least 2.")
            break
        except ValueError as error:
            print(error)

    # tạo list các điểm
    points = get_coordinates(n)

    distance = calculate_euclidean_distance_between_points(points)
    print("The sum of the Euclidean distances between the points is:", distance)

except ValueError as error:
    print(error)