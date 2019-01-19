from unittest import TestCase

from sum_of_numbers.src.math_operator import MathOperator


class TestMathOperator(TestCase):

    # Name of the method: sum
    # What it is supposed to do: returns the sum of two number
    # Conditions: input numbers are positive
    def test__sum__returns_the_sum_of_two_numbers__when_both_numbers_are_positive(self):
        math_operator = MathOperator()

        actual_sum = math_operator.add(3, 5)

        assert actual_sum == 8
