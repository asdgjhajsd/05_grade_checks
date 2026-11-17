import pytest

from src.grade_average import calculate_average


@pytest.mark.parametrize(
    "mark_one, mark_two, expected",
    [
        (0, 0, 0),
        (100, 100, 100),
        (50, 50, 50),
        (50, 51, 50.5),
    ],
)
def test_calculate_average_valid_marks_returns_expected_average(
    mark_one,
    mark_two,
    expected,
):
    # Arrange

    # Act
    result = calculate_average(mark_one, mark_two)

    # Assert
    assert result == expected


@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        ("50", 50),
        (50, "50"),
        (None, 50),
        (50, None),
        (True, 50),
    ],
)
def test_calculate_average_invalid_type_raises_type_error(
    mark_one,
    mark_two,
):
    with pytest.raises(TypeError):
        calculate_average(mark_one, mark_two)


@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        (-1, 50),
        (101, 50),
        (50, -1),
        (50, 101),
    ],
)
def test_calculate_average_out_of_range_raises_value_error(
    mark_one,
    mark_two,
):
    with pytest.raises(ValueError):
        calculate_average(mark_one, mark_two)