from math import sqrt, acos, pi, dist,sin

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
    """
    Checks whether or not there exists at least one set of [n_pts] consecutive data points such that at least one point 
    lies at a distance greater than [dist] to the line joining the first and the last point.
    If the first and last point are the same, then it will check whether or not *all* other points lie at a distance
    greater than [dist] to the first/last point. 
    """
    n_pts = parameters["n_pts"]
    dist_p = parameters["dist"]

    if len(points) < n_pts or len(points) < 3:
        return False

    for i in range(len(points)-n_pts+1):
        consecutive_points = []
        for j in range(n_pts):
            consecutive_points.append(points[i+j])
        p1 = consecutive_points[0]
        p2 = consecutive_points[-1]
        line = dist(p1, p2)
        all_points_greater_than_dist = True # used in case p1 and p2 are the same
        for p in consecutive_points[1:-1]:
            if line == 0:
                dist_to_point = dist(p, p1)
                if dist_to_point < dist_p:
                    all_points_greater_than_dist = False
                    break
            else:
                dist_to_line = abs((p2[0]-p1[0])*(p1[1]-p[1]) - (p1[0]-p[0])*(p2[1]-p1[1]))/line
                if dist_to_line > dist_p:
                    return True
        if line == 0 and all_points_greater_than_dist:
            return True
    return False

def lic_7(parameters, points):
    """
    Checks whether or not there exists two points separated by [k_pts] consecutive points
    that are more than [length1] units apart
    """
    k_pts = parameters["k_pts"]
    length1 = parameters["length1"]

    for i in range(len(points)-k_pts-1):
        if dist(points[i], points[i+k_pts+1]) > length1:
            return True
    return False

def lic_8(parameters, points):
    """
    Checks if there exists at least one set of three datapoints separated by exaclty A_PTS and B_PTS *consecutive* intervening points,
    respectively, that cannot be contained within or on a circle of RADIUS1. The condition is not met NUMPOINTS < 5.
    1 <= A_PTS, 1 <= B_PTS
    A_PTS + B_PTS <= NUMPOINTS - 3
    """
    a_pts = parameters["a_pts"]
    b_pts = parameters["b_pts"]
    radius1 = parameters["radius1"]

    if(len(points) < 5 or a_pts < 1 or b_pts < 1):
        return False
    elif((a_pts + b_pts) > (len(points)-3)):
        return False
    radius1 = parameters["radius1"]

    for i in range(len(points)):
        if(a_pts + b_pts + i + 2 > len(points)-1):
            break
        x1 = points[i][0] 
        y1 = points[i][1]
        x2 = points[i + a_pts + 1][0]
        y2 = points[i + a_pts + 1][1]
        x3 = points[i + a_pts + b_pts + 2][0]
        y3 = points[i + a_pts + b_pts + 2][1]

        if smallest_Radius(x1, y1, x2, y2, x3, y3,radius1):
            return True
    return False


def lic_9(parameters, points):
    """
    There exists at least one set of three data points separated by exactly C_PTS and D_PTS *consecutive* intervening points, respectively,
    that form an angle such that:
    
    angle < pi-epsilon

    angle > pi + epsilon
  
    The second point of the set of three points is always the vertex of the angle. If either the first or the last point or both coincide with
    the vertex the angle is undefined and the LIC is not satisfied by those three points.
    
     When NUMPOINTS < 5 the condition is not met
     1<= C_PTS,1 <= D_PTS

     C_PTS + D_PTS <= NUMPOINTS - 3
    """
    c_pts = parameters["c_pts"]
    d_pts = parameters["d_pts"]
    epsilon = parameters["epsilon"]

    if(len(points) < 5 or c_pts < 1 or d_pts < 1 or c_pts + d_pts <= len(points)-3):

        for i in range(len(points)-2-c_pts-d_pts):

            a = (points[i][0], points[i][1])
            v = (points[i + c_pts + 1][0], points[i + c_pts + 1][1])
            b = (points[i + c_pts + d_pts + 2][0], points[i + c_pts + d_pts + 2][1])

            if a != v and b != v:
                va = sqrt((a[0] - v[0])**2 + (a[1] - v[1])**2)
                vb = sqrt((b[0] - v[0])**2 + (b[1] - v[1])**2)
                vc = sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

                angle = acos((va**2 + vb**2 - vc**2 )/(2*va*vb))

                if (angle < pi - epsilon)  or (angle > pi + epsilon):
                    return True
    return False

def lic_10(parameters, points):
    # TODO: Implement
    pass

def lic_11(parameters, points):
    # TODO: Implement
    pass

def lic_12(parameters, points):
    if len(points) < 3 or parameters["length2"] <= 0.0:
        return False

    k_pts = parameters["k_pts"]
    length1 = parameters["length1"]
    length2 = parameters["length2"]

    long_points = False
    short_points = False
    for i in range(len(points) - k_pts - 1):
        for j in range(i + k_pts + 1, len(points)):
            distance = sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            if distance > length1:
                long_points = True
            if distance < length2:
                short_points = True
            if long_points and short_points:
                return True
    return False
    
def lic_13(parameters, points):
    # TODO: Implement
    pass

def lic_14(parameters, points):
    # TODO: Implement
    pass

def smallest_Radius(x1,y1,x2,y2,x3,y3,radius):
    
    d1 = abs(sqrt((x1-x2)**2 + (y1-y2)**2))
    d2 = abs(sqrt((x2-x3)**2 + (y2-y3)**2))
    d3 = abs(sqrt((x1-x3)**2 + (y1-y3)**2))

    #check if one or more point is the same
    if((d1 == 0) or (d2 == 0) or (d3 == 0)):
        return max(d1,d2,d3)/2 <= radius
    #check if big angle
    a = acos((d2*d2 + d3*d3 - d1*d1)/(2*d2*d3))
    b = acos((d1*d1 + d3*d3 - d2*d2)/(2*d1*d3))
    c = acos((d2*d2 + d1*d1 - d3*d3)/(2*d2*d1))

    if(a > pi/2 or b > pi/2 or c > pi/2):
        return max(d1,d2,d3)/2 <= radius
    else:
    #https://mathalino.com/reviewer/derivation-of-formulas/derivation-of-formula-for-radius-of-circumcircle

        return d1/(2*sin(a)) <= radius
