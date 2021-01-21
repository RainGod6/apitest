from common.number import Number
import pytest


class TestNumber:

    @pytest.mark.parametrize("a,b,res", {
        (0, 100, 100),
        (2, 3, 5),
        (3.2, 1.3, 4.5)
    })
    def test_add(self, a, b, res):
        result = Number().add(a, b)
        assert result == res

    @pytest.mark.parametrize("a,b,res",{
        (10,0,10),
        (100,99,1),
        (0,0,0),
        (10.9,9.1,1.8)
    })
    def test_subtraction(self, a, b,res):
        result = Number().subtraction(a,b)
        assert result == res

    @pytest.mark.parametrize("a,b,res",{
        (1,3,3),
        (5,50,250),
        (0,3,0)
    })
    def test_multiplication(self, a, b,res):
        result = Number().multiplication(a,b)
        assert result == res

    @pytest.mark.parametrize("a,b,res",{
        (4,2,2),
        (8,4.0,2),
        (1000,100,10)
    })
    def test_division(self, a, b,res):
        result = Number().division(a,b)
        assert result == res
