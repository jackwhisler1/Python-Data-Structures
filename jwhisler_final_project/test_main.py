from main import validate_date


def test_validate_date_valid():
    """Should pass with correctly formatted date."""
    try:
        validate_date("10-15-2025")
    except ValueError:
        assert False, "validate_date raised ValueError on a valid date."


def test_validate_date_invalid():
    """Should raise ValueError with invalid format."""
    try:
        validate_date("2025-10-15")
        assert False, "validate_date did not raise ValueError for invalid format."
    except ValueError as e:
        assert str(
            e) == "Date must be formatted as MM-DD-YYYY.", "Unexpected error message."


if __name__ == "__main__":
    test_validate_date_valid()
    test_validate_date_invalid()
    print("All date validation tests passed.")
