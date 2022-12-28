def distance_between_two_points(x1, y1, x2, y2):


    import math

    result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return result


print(distance_between_two_points(2, 4, 3, 3))