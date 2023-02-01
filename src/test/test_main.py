from src.main import *
from math import pi
import pytest

def create_valid_input():
    """
    Returns a set of valid test data
    """
    num_points = 10
    points = []
    for i in range(num_points):
        points.append((i, i))
    parameters = {
        "length1": 1,      # Length in LICs 0, 7, 12
        "radius1": 1,      # Radius in LICs 1, 8, 13
        "epsilon": 0.5,      # Deviation from PI in LIC 2,9
        "area1": 1,        # Area in LICs 3, 10, 14
        "q_pts": 2,          # Nr consecutive points in LIC 4
        "quads": 2,          # Nr quadrants in LIC 4
        "dist": 1,         # Distance in LIC 6
        "n_pts": 3,          # Nr consecutive points in LIC 6
        "k_pts": 2,          # Nr int points in LICS 7, 12
        "a_pts": 1,          # Nr int points in LICS 8, 13
        "b_pts": 1,          # Nr int points in LICS 8, 13
        "c_pts": 1,          # Nr int points in LICS 9
        "d_pts": 1,          # Nr int points in LICS 9
        "e_pts": 1,          # Nr int points in LICS 10, 14
        "f_pts": 1,          # Nr int points in LICS 10, 14
        "g_pts": 1,          # Nr int points in LICS 11
        "length2": 1,      # Nr int points in LICS 12
        "radius2": 1,      # Nr int points in LICS 13
        "area2": 1,        # Nr int points in LICS 14
    }

    lcm = []
    puv = []
    for i in range(15):
        puv.append([True]*15)
        lcm.append(["ANDD"]*15)
    
    return num_points, points, parameters, lcm, puv

def test_validate_input_too_few_points():
    """
    Tests that an exception is raised when there are less than 2 data points
    """
    num_points, points, parameters, lcm, puv = create_valid_input()

    num_points = 1
    points = [(0.0, 0.0)]

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_too_many_points():
    """
    Tests that an exception is raised when there are more than 100 data points
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    num_points = 101
    points = [(0.0, 0.0)] * num_points

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_num_points_not_equal_to_points():
    """
    Tests that an exception is raised when num_points != len(points)
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    num_points = len(points) - 1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_negative_length1():
    """
    Tests that an exception is raised when length1 < 0
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["length1"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_negative_radius1():
    """
    Tests that an exception is raised when radius1 < 0
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["radius1"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_negative_epsilon():
    """
    Tests that an exception is raised when epsilon < 0
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["epsilon"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_negative_epsilon_equals_pi():
    """
    Tests that an exception is raised when epsilon >= pi
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["epsilon"] = pi

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_negative_area1():
    """
    Tests that an exception is raised when area1 < 0
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["area1"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_q_pts_too_small():
    """
    Tests that an exception is raised when q_pts < 2
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["q_PTS"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_q_pts_too_big():
    """
    Tests that an exception is raised when q_pts > num_points
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["q_PTS"] = num_points + 1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_quads_too_small():
    """
    Tests that an exception is raised when quads < 1
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["quads"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_quads_too_big():
    """
    Tests that an exception is raised when quads > 3
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["quads"] = 4

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_too_small():
    """
    Tests that an exception is raised when dist < 0
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["dist"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_n_pts_too_small():
    """
    Tests that an exception is raised when n_pts < 3
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["n_pts"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_n_pts_too_big():
    """
    Tests that an exception is raised when n_pts > num_points
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["n_pts"] = num_points + 1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_k_pts_too_big():
    """
    Tests that an exception is raised when k_pts > num_points - 2
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["k_pts"] = num_points - 1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_k_pts_too_small():
    """
    Tests that an exception is raised when k_pts < 1
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["k_pts"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_a_pts_too_small():
    """
    Tests that an exception is raised when a_pts < 1
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["a_pts"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_b_pts_too_small():
    """
    Tests that an exception is raised when b_pts < 1
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["b_pts"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_a_b_pts_too_big():
    """
    Tests that an exception is raised when a_pts + b_pts > num_points - 3
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["b_pts"] = num_points
    parameters["a_pts"] = num_points

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_c_pts_too_small():
    """
    Tests that an exception is raised when c_pts < 1
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["c_pts"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_d_pts_too_small():
    """
    Tests that an exception is raised when d_pts < 1
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["d_pts"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

        
def test_validate_input_dist_c_d_pts_too_big():
    """
    Tests that an exception is raised when c_pts + d_pts > num_points - 3
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["c_pts"] = num_points
    parameters["d_pts"] = num_points

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_e_pts_too_small():
    """
    Tests that an exception is raised when e_pts < 1
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["e_pts"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_f_pts_too_small():
    """
    Tests that an exception is raised when f_pts < 1
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["f_pts"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_dist_e_f_pts_too_big():
    """
    Tests that an exception is raised when e_pts + f_pts > num_points - 3
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["e_pts"] = num_points
    parameters["f_pts"] = num_points

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_g_pts_too_small():
    """
    Tests that an exception is raised when g_pts < 1
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["g_pts"] = 0

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_g_pts_too_big():
    """
    Tests that an exception is raised when g_pts > num_points - 2
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["g_pts"] = num_points - 1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_length2_too_small():
    """
    Tests that an exception is raised when length2 < 0
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["length2"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_radius2_too_small():
    """
    Tests that an exception is raised when radius2 < 0
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["radius2"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)

def test_validate_input_area2_too_small():
    """
    Tests that an exception is raised when area2 < 0
    """
    num_points, points, parameters, lcm, puv = create_valid_input()
    parameters["area2"] = -1

    with pytest.raises(Exception):
        validate_input(num_points, points, parameters, lcm)