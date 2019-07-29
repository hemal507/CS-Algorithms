import sameDigitNumber
import pytest

@pytest.fixture(scope='module')
def test_case1() :
    assert sameDigitNumber.sameDigitNumber(1111) == True

def test_case2() :
    assert sameDigitNumber.sameDigitNumber(1121) == False
