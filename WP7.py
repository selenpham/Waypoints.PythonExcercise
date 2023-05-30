# Waypoint 7: Calculate Distance between two 2D Points
# Write a function calculate_euclidean_distance_between_2_points that takes two arguments p1 and p2, 
# representing points in a two-dimensional Cartesian coordinate system, and that returns the Euclidean distance between p1 and p2.

# The arguments p1 and p2 are each represented with a tuple of 2 integers or floats (x, y) where x corresponds to the position of 
# the point on the X-axe (i.e, abscissa), and y corresponds to the position of the point on the Y-axe (i.e., ordinate).
# For examples:
# >>> calculate_euclidean_distance_between_2_points((1, 2), (1, 2))
# 0.0
# >>> calculate_euclidean_distance_between_2_points((0, 0), (3, 4))
# 5.0
# >>> calculate_euclidean_distance_between_2_points((1, 1), (2, 2))
# 1.4142135623730951

# ********************************************
# B1. Tạo hàm tính khoảng cách giữa 2 điểm, p1,p2 trên mặt phẳng.
# Sử dụng công thức pytago

def calculate_euclidean_distance_between_2_points(p1, p2):
    distance = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
    return distance

# B2: tạo hàm nhập 1 điểm bất kì có 2 tọa độ x,y. 
# Tạo ràng buộc tọa độ là số. tạo vòng lặp để nhập cho tới khi thỏa mãn điều kiện
def get_coordinates():
    while True:
        try:
            x = float(input("Enter the x-coordinate: "))
            y = float(input("Enter the y-coordinate: "))
            return (x, y)
        except ValueError:
            print("Invalid input, please enter a number for the coordinates.")

#B3. nhập giá trị p1, giá giá trị p1 bằng hàm get_coordinates
print("Enter coordinates for point 1:")
p1 = get_coordinates()

#B4. nhập giá trị p21, giá giá trị p2 bằng hàm get_coordinates
print("Enter coordinates for point 2:")
p2 = get_coordinates()

#B5. Tính khoảng cách euclindean giữa 2 điểm
distance = calculate_euclidean_distance_between_2_points(p1, p2)
print("The Euclidean distance between the two points is:", distance)