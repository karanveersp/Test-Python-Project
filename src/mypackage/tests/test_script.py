from mypackage import script

def test_add_works():
    # Arrange
    x, y = 1, 2
    expected = 3

    # Act
    actual = script.add(x, y)

    # Assert
    assert actual == expected