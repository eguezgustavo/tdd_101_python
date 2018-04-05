from unittest import TestCase
from nose.tools import assert_equals, istest
from suma import suma


class SumaTest(TestCase):

    @istest
    def suma__return_the_sum__when_both_numbers_are_positive(self):
        a = 5
        b = 4

        result = suma(a, b)

        assert_equals(9, result)

