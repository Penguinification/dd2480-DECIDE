from ast import literal_eval

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

    launch, cmv, pum, fuv = decide(num_points, points, parameters, lcm, puv)
    if launch:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
