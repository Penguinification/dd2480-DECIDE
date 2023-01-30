from pum import *

def test_pum_andd():
    """
    Tests that pum returns a 15x15 vector with correct values when the ANDD operator is used in the lcm.
    When both cmv[i] and cmv[j] are true, pum[i][j] should be true. If not, then pum[i][j] should be false.
    """
    lcm = [["ANDD" for _ in range(15)] for _ in range(15)]
    cmv = [True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]
    result = pum(lcm, cmv)
    for i in range(len(cmv)):
        for j in range(len(cmv)):
            if i % 2 == 0 and j % 2 == 0:
                assert(result[i][j])
            else:
                assert(not result[i][j])

def test_pum_orr():
    """
    Tests that pum returns a 15x15 vector with correct values when the ORR operator is used in the lcm.
    When neither cmv[i] nor cmv[j] are true, pum[i][j] should be false. Otherwise, pum[i][j] should be true.
    """
    lcm = [["ORR" for _ in range(15)] for _ in range(15)]
    cmv = [True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]
    result = pum(lcm, cmv)
    for i in range(len(cmv)):
        for j in range(len(cmv)):
            if i % 2 == 1 and j % 2 == 1:
                assert(not result[i][j])
            else:
                assert(result[i][j])

def test_pum_notused():
    """
    Tests that pum correctly returns a 15x15 vector filled with the boolean false when the NOTUSED operator
    is the only operator used in the lcm.
    """
    lcm = [["NOTUSED" for _ in range(15)] for _ in range(15)]
    cmv = [True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]
    result = pum(lcm, cmv)
    expected = [[True] * 15] * 15
    assert(result == expected)
