from math import sqrt

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
    # TODO: Implement
    pass

def lic_2(parameters, points):
    # TODO: Implement
    pass

def lic_3(parameters, points):
    # TODO: Implement
    pass

def lic_4(parameters, points):
    # TODO: Implement
    pass

def lic_5(parameters, points):
    # TODO: Implement
    pass

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