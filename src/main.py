from ast import literal_eval
from math import pi

def decide(num_points, points, parameters, lcm, puv):
    # TODO: Implement function
    launch = False
    cmv = {}
    pum = {}
    fuv = {}
    
    output = (launch, cmv, pum, fuv)
    return output

def main():
    num_points = int(input())
    points = list()
    for _ in range(0, num_points):
        elem = literal_eval(input())
        points.append(elem)
    parameters = {
        "length1": float(input()),      # Length in LICs 0, 7, 12
        "radius1": float(input()),      # Radius in LICs 1, 8, 13
        "epsilon": float(input()),      # Deviation from PI in LIC 2,9
        "area1": float(input()),        # Area in LICs 3, 10, 14
        "q_pts": int(input()),          # Nr consecutive points in LIC 4
        "quads": int(input()),          # Nr quadrants in LIC 4
        "dist": float(input()),         # Distance in LIC 6
        "n_pts": int(input()),          # Nr consecutive points in LIC 6
        "k_pts": int(input()),          # Nr int points in LICS 7, 12
        "a_pts": int(input()),          # Nr int points in LICS 8, 13
        "b_pts": int(input()),          # Nr int points in LICS 8, 13
        "c_pts": int(input()),          # Nr int points in LICS 9
        "d_pts": int(input()),          # Nr int points in LICS 9
        "e_pts": int(input()),          # Nr int points in LICS 10, 14
        "f_pts": int(input()),          # Nr int points in LICS 10, 14
        "g_pts": int(input()),          # Nr int points in LICS 11
        "length2": float(input()),      # Nr int points in LICS 12
        "radius2": float(input()),      # Nr int points in LICS 13
        "area2": float(input()),        # Nr int points in LICS 14
    }
    lcm  = [[input() for _ in range(15)] for _ in range(15)] #15x15 matrix AND, OR, notatall

    puv = [[bool(input()) for _ in range(15)] for _ in range(15)]

    validate_input(num_points, points, parameters, lcm)

    launch, cmv, pum, fuv = decide(num_points, points, parameters, lcm, puv)
    if launch:
        print("YES")
    else:
        print("NO")

def validate_input(num_points, points, parameters, lcm):
    """
    Makes sure that all inputs are within their allowed bounds/types as given by the specification,
    raises an exception if a parameter is invalid
    """    
    if num_points < 2:
        raise Exception("Too few data points")
    if num_points > 100:
        raise Exception("Too many data points")
    if len(points) != num_points:
        raise Exception("Incorrect amount of data points")
    if parameters["length1"] < 0:
        raise Exception("length1 parameter needs to be greater than or equal to 0")
    if parameters["radius1"] < 0:
        raise Exception("radius1 parameter needs to be greater than or equal to 0")
    if parameters["epsilon"] < 0:
        raise Exception("epsilon parameter needs to be greater than or equal to 0")
    if parameters["epsilon"] >= pi:
        raise Exception("epsilon parameter needs to be less than pi")
    if parameters["area1"] < 0:
        raise Exception("area1 parameter needs to be greater than or equal to 0")
    if parameters["q_pts"] < 2:
        raise Exception("q_pts parameter needs to be greater than or equal to 2")
    if parameters["q_pts"] > num_points:
        raise Exception("q_pts parameter cannot be greater than num_points")
    if parameters["quads"] < 1:
        raise Exception("quads parameter needs to be greater than or equal to 1")
    if parameters["quads"] > 3:
        raise Exception("quads parameter needs to be less than 4")
    if parameters["dist"] < 0:
        raise Exception("dist parameter needs to be greater than or equal to 0")
    if parameters["n_pts"] < 3:
        raise Exception("n_pts parameter needs to be greater than 2")
    if parameters["n_pts"] > num_points:
        raise Exception("n_pts parameter needs to be less than or equal to num_points")
    if parameters["k_pts"] < 1:
        raise Exception("k_pts parameter needs to be greater than 0")
    if parameters["k_pts"] > (num_points - 2):
        raise Exception("k_pts parameter needs to be less than or equal to num_points - 2")
    if parameters["a_pts"] < 1:
        raise Exception("a_pts parameter needs to be greater than 0")
    if parameters["b_pts"] < 1:
        raise Exception("b_pts parameter needs to be greater than 0")
    if parameters["a_pts"] + parameters["b_pts"] > (num_points - 3):
        raise Exception("a_pts + b_pts cannot be greater than num_points - 3")
    if parameters["c_pts"] < 1:
        raise Exception("c_pts parameter needs to be greater than 0")
    if parameters["d_pts"] < 1:
        raise Exception("d_pts parameter needs to be greater than 0")
    if parameters["c_pts"] + parameters["d_pts"] > (num_points - 3):
        raise Exception("c_pts + d_pts cannot be greater than num_points - 3")
    if parameters["e_pts"] < 1:
        raise Exception("e_pts parameter needs to be greater than 0")
    if parameters["f_pts"] < 1:
        raise Exception("f_pts parameter needs to be greater than 0")
    if parameters["e_pts"] + parameters["f_pts"] > (num_points - 3):
        raise Exception("e_pts + f_pts cannot be greater than num_points - 3")
    if parameters["g_pts"] < 1:
        raise Exception("g_pts parameter needs to be greater than 0")
    if parameters["g_pts"] > (num_points - 2):
        raise Exception("g_pts parameter needs to be less than or equal to num_points - 2")
    if parameters["length2"] < 0:
        raise Exception("length2 parameter needs to be greater than or equal to 0")
    if parameters["radius2"] < 0:
        raise Exception("radius2 parameter needs to be greater than or equal to 0")
    if parameters["area2"] < 0:
        raise Exception("area2 parameter needs to be greater than or equal to 0")

    for i in range(15):
        for j in range(15):
            if lcm[i][j] != "ANDD" or lcm[i][j] != "ORR" or lcm[i][j] != "NOTUSED":
                raise Exception(f"invalid element in lcm[{i}][{j}]")
            


if __name__ == "__main__":
    main()
