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

def test_lic_0_true():
    """""
    Test that lic_0 returns true when two consecutive points have a distance larger than or equal to length1
    """""
    parameters = {
        "length1": 0.5
    }
    points = [(0.0, 0.0), (0.0, 0.0), (1.0, 1.0)]
    result = lic_0(parameters, points)
    assert(result)

def test_lic_0_false():
    """""
    Test that lic_0 returns false when no consecutive points have a distance larger than or equal to length1
    """""
    parameters = {
        "length1": 5.0
    }
    points = [(0.0, 0.0), (1.0, 1.0), (1.0, 3.0)]
    result = lic_0(parameters, points)
    assert(not result)

def test_lic_2_true():
    """
    Test that lic_2 returns true when angle < (PI-EPSILON) (or equivalently outer angle > (PI+EPSILON))
    """
    parameters = {
        "epsilon": pi/2
    }
    points = [(0.0, 0.0), (1.0, 0.0), (0, 1.0)] # pi/4 angle
    result = lic_2(parameters, points)
    assert(result)


def test_lic_2_false():
    """
    Test that lic_2 returns false when angle > (PI-EPSILON) (or equivalently outer angle < (PI+EPSILON))
    """
    parameters = {
        "epsilon": pi
    }
    points = [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0)] # pi/2 angle
    result = lic_2(parameters, points)
    assert(not result)

def test_lic_2_coinciding_vertex_1():
    """
    Test that lic_2 returns false when the first point in one sequence
    coincides with the vertex and no other sequence of consecutive points
    satisfies angle < (PI-EPSILON)
    """
    parameters = {
        "epsilon": pi
    }
    points = [(0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (1.0, 1.0)]
    result = lic_2(parameters, points)
    assert(not result)

def test_lic_2_coinciding_vertex_2():
    """
    Test that lic_2 returns true when the first point in one sequence
    coincides with the vertex and another sequence of consecutive points
    satisfies angle < (PI-EPSILON)
    """
    parameters = {
        "epsilon": pi/2
    }
    points = [(0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (0, 1.0)]
    result = lic_2(parameters, points)
    assert(result)

def test_lic_2_coinciding_vertex_3():
    """
    Test that lic_2 returns false when the last point in one sequence
    coincides with the vertex and no other sequence of consecutive points
    satisfies angle < (PI-EPSILON)
    """
    parameters = {
        "epsilon": pi
    }
    points = [(-1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (1.0, 1.0)]
    result = lic_2(parameters, points)
    assert(not result)

def test_lic_2_coinciding_vertex_4():
    """
    Test that lic_2 returns true when the last point in one sequence
    coincides with the vertex and another sequence of consecutive points
    satisfies angle < (PI-EPSILON)
    """
    parameters = {
        "epsilon": pi/2
    }
    points = [(-1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (0, 1.0)]
    result = lic_2(parameters, points)
    assert(result)

def test_lic_3_true():
    """
    Tests that lic_3 returns true when there are three consecutive points that form a triangle
    with area > [area1]
    """
    parameters = {
        "area1": 0.5
    }
    points = [(0.0, 0.0), (2.0, 0.0), (2.0, 2.0)]
    result = lic_3(parameters, points)
    assert result

def test_lic_3_false_area_too_small():
    """
    Tests that lic_3 returns false when the area of the triangle is smaller than [area1]
    """
    parameters = {
        "area1": 2.0
    }
    points = [(0.0, 0.0), (1.0, 0.0), (0.0, 0.5)]
    result = lic_3(parameters, points)
    assert not result

def test_lic_3_false_too_few_points():
    """
    Tests that lic_3 returns false when there are only two data points
    """
    parameters = {
        "area1": 0.5
    }
    points = [(0.0, 0.0), (2.0, 0.0)]
    result = lic_3(parameters, points)
    assert not result

def test_lic_3_false_not_a_triangle():
    """
    Tests that lic_3 returns false when the points don't form a triangle
    """
    parameters = {
        "area1": 0.5
    }
    points = [(0.0, 0.0), (0.0, 0.0), (5.0, 5.0)]
    result = lic_3(parameters, points)
    assert not result
