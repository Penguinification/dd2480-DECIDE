from math import sqrt, acos, pi, dist

def cmv(parameters, points):
    cmv = [False] * 15
    cmv[0] = lic_0(parameters, points)
    cmv[1] = lic_1(parameters, points)
    cmv[2] = lic_2(parameters, points)
    cmv[3] = lic_3(parameters, points)
    cmv[4] = lic_4(parameters, points)
    cmv[5] = lic_5(parameters, points)
    cmv[6] = lic_6(parameters, points)
    cmv[7] = lic_7(parameters, points)
    cmv[8] = lic_8(parameters, points)
    cmv[9] = lic_9(parameters, points)
    cmv[10] = lic_10(parameters, points)
    cmv[11] = lic_11(parameters, points)
    cmv[12] = lic_12(parameters, points)
    cmv[13] = lic_13(parameters, points)
    cmv[14] = lic_14(parameters, points)
    return cmv

def lic_0(parameters, points):
    for i in range(0, len(points)-1):
        x_distance = abs(points[i][0] - points[i+1][0])
        y_distance = abs(points[i][1] - points[i+1][1])
        distance = abs(sqrt(x_distance**2 + y_distance**2))
        if distance > parameters["length1"]:
            return True
    return False

def lic_1(parameters, points):
    """
    Checks whether any three data points fits inside a circle
    with the radius specified in parameters["radius1"]
    """
    for i in range(len(points) - 2):
        p1 = points[i]
        p2 = points[i+1]
        p3 = points[i+2]

        a = dist(p1, p2)
        b = dist(p1, p3)
        c = dist(p2, p3)

        # Semi-perimeter
        s = (a+b+c)/2

        # Heron's formula
        area = sqrt(s*(s-a)*(s-b)*(s-c))
        
        # If the area is zero, then the triangle is degenerate, i.e. a+b=c for a≤b≤c
        if area == 0.0:
            if max(a, b, c) > 2*parameters["radius1"]:
                return True
            else:
                continue
        
        # All other triangles
        circumradius = a*b*c/(4*area)

        if circumradius > parameters["radius1"]:
            return True
    return False

def lic_2(parameters, points):
    for i in range(0, len(points)-2):
        a_x_distance = abs(points[i+1][0] - points[i+2][0])
        a_y_distance = abs(points[i+1][1] - points[i+2][1])
        a = abs(sqrt(a_x_distance**2 + a_y_distance**2))

        b_x_distance = abs(points[i][0] - points[i+1][0])
        b_y_distance = abs(points[i][1] - points[i+1][1])
        b = abs(sqrt(b_x_distance**2 + b_y_distance**2))

        c_x_distance = abs(points[i][0] - points[i+2][0])
        c_y_distance = abs(points[i][1] - points[i+2][1])
        c = abs(sqrt(c_x_distance**2 + c_y_distance**2))

        # Not satisfied if either the first point or
        # the last point (or both) coincides with the vertex
        if a == 0 or b == 0:
            continue
        
        # Use the law of cosines
        angle = acos((a**2 + b**2 - c**2) / (2*a*b))

        if angle < pi - parameters["epsilon"]:
            return True
    return False

def lic_3(parameters, points):
    """
    Checks whether or not there are three consecutive points that form a triangle with area greater than [area1].
    Uses Heron's formula to calculate the area of the triangle created by three consecutive points. 
    """
    if len(points) < 3:
        return False

    area1 = parameters["area1"]

    for i in range(len(points)-2):
        p1 = points[i]
        p2 = points[i+1]
        p3 = points[i+2]
        a = dist(p1, p2)
        b = dist(p1, p3)
        c = dist(p2, p3)
        s = (a+b+c)/2
        area = sqrt(s*(s-a)*(s-b)*(s-c))
        if area > area1:
            return True
    return False

def lic_4(parameters, points):
    """
    Checks whether or not there exists a set of [q_pts] consecutive points that lie in more than [quads] quadrants.
    """
    q_pts = parameters["q_pts"]
    quads = parameters["quads"]
    
    if len(points) < q_pts:
        return False

    for i in range(len(points)-q_pts+1):
        consecutive_points = []
        for j in range(q_pts):
            consecutive_points.append(points[i+j])
        
        counts = [0,0,0,0] # q1, q2, q3, q4
        for point in consecutive_points:
            if point[0] > 0 and point[1] > 0:
                counts[0] += 1
            elif point[0] < 0 and point[1] > 0:
                counts[1] += 1
            elif point[0] < 0 and point[1] < 0:
                counts[2] += 1
            elif point[0] > 0 and point[1] < 0:
                counts[3] += 1
            else: # cases where a point is on either of the axes
                if point[0] == 0: # point is on the y axis
                    if point[1] >= 0:
                        counts[0] += 1
                    else:
                        counts[2] += 1
                else: # point is on the x axis
                    if point[0] >= 0:
                        counts[0] += 1
                    else:
                        counts[1] += 1
        different_quads = 0
        for i in counts:
            if i > 0:
                different_quads += 1
        if different_quads > quads:
            return True
    return False

def lic_5(parameters, points):
    """
    Checks whether there exists two consecutive points (x1, y1) (x2, y2) such that x2 - x1 < 0
    """
    for i in range(0, len(points)-1):
        if points[i+1][0] - points[i][0] < 0:
            return True
    return False

def lic_6(parameters, points):
    # TODO: Implement
    pass

def lic_7(parameters, points):
    # TODO: Implement
    pass

def lic_8(parameters, points):
    # TODO: Implement
    pass

def lic_9(parameters, points):
    # TODO: Implement
    pass

def lic_10(parameters, points):
    # TODO: Implement
    pass

def lic_11(parameters, points):
    # TODO: Implement
    pass

def lic_12(parameters, points):
    # TODO: Implement
    pass

def lic_13(parameters, points):
    # TODO: Implement
    pass

def lic_14(parameters, points):
    # TODO: Implement
    pass