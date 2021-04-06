from app.resources.predict.helpers import double_value


def test_double_value():
    """Test the double value function."""
    starting_list = [1, 2, 3, 4, 5]
    ending_list = [2, 4, 6, 8, 10]
    for i, number in enumerate(starting_list):
        assert double_value(number) == ending_list[i]
