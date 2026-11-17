import pytest

from src.grade_pass import has_passed


@pytest.mark.parametrize(
    "score, expected",
    [
        (0, False),
        (49, False),
        (50, True),
        (75, True),
        (100, True),
    ],
)
def test_has_passed_valid_score_returns_expected_result(
    score,
    expected,
):
    # Act
    result = has_passed(score)

    # Assert
    assert result is expected


@pytest.mark.parametrize(
    "score",
    [
        "50",
        None,
        True,
    ],
)
def test_has_passed_invalid_type_raises_type_error(score):
    with pytest.raises(TypeError):
        has_passed(score)


@pytest.mark.parametrize(
    "score",
    [
        -1,
        101,
    ],
)
def test_has_passed_out_of_range_raises_value_error(score):
    with pytest.raises(ValueError):
        has_passed(score)