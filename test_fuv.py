from fuv import *

def test_fuv():
    """
    Tests that the FUV is created correctly:
        * FUV is true if PUV is false
        * FUV is false if PUM[i] is not all true
        * FUV is true if PUM[i] is all true
    """
    row = [True, False]*7
    row.append(True)
    puv = row
    pum = []
    for i in range(14):
        pum.append(row)
    pum.append([True]*15)
    fuv_res = fuv(puv, pum)
    for i in range(14):
        if i % 2 == 0:
            assert not fuv_res[i] # row is not all true so FUV is false
        else:
            assert fuv_res[i] # PUV is false so FUV is true
    assert fuv_res[14] # last row is all true