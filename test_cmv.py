from math import pi
from cmv import *

def test_cmv():
    """""
    Tests that the 'cmv' function returns the same vector
    as calling every 'lic' function individually would
    """""
    points = list()
    for i in range(0, 100):
        points.append((i, i))

    parameters = {
        "length1": 0.5,
        "radius1": 10.0,
        "epsilon": pi/2,
        "area1": 10.0,
        "q_pts": 10,
        "quads": 5,
        "dist": 5.0,
        "n_pts": 5,
        "k_pts": 5,
        "a_pts": 5,
        "b_pts": 5,
        "c_pts": 5,
        "d_pts": 5,
        "e_pts": 5,
        "f_pts": 5,
        "g_pts": 5,
        "length2": 10.0,
        "radius2": 5.0,
        "area2": 10.0
    }

    cmv_res = cmv(parameters, points)
    lics = [lic_0, lic_1, lic_2, lic_3, lic_4, lic_5, lic_6, lic_7, lic_8, lic_9, lic_10, lic_11, lic_12, lic_13, lic_14]
    for i in range(15):
        assert cmv_res[i] == lics[i](parameters, points)
