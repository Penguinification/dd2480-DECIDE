from src.launch import launch

def test_launch_true():
    """
    Tests that launch returns true if all elements in the fuv are true
    """
    fuv = [True] * 15
    result = launch(fuv)
    assert(result)

def test_launch_false():
    """
    Tests that launch returns false if the fuc contains false elements
    """
    fuv = [int(i % 2) for i in range(15)]
    result = launch(fuv)
    assert(not result)
