import pytest

from python.calc import Calc


class TestCalc:

    def setup(self):
        self.calc = Calc()


    def test_add(self):
        assert self.calc.add(1,2) == 3

    def test_div(self):
        assert self.calc.div(1,2) == 0.5

    def test_add2(self):
        data = (1,2)
        assert  self.calc.add2(data)
        assert  self.calc.add(*data)


if __name__ == '__main__':
    pytest.main("-v -s")
