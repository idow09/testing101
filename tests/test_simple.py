import numpy as np


def test_mean():
    # Arrange
    data = [1, 2, 3, 4, 5]

    # Act
    result = np.mean(data)

    # Assert
    assert result == 3
