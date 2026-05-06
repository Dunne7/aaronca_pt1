import pytest
import sys
#Issues with path so had to implement
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from part1 import *

"Unit tests for part1 function"

#calculate interest for Tier 1 to 4
def test_interest_tier1_deposit():
    result = calculate_interest(500)
    assert result == "15.00"


def test_interest_tier2_deposit():
    result = calculate_interest(6000)
    assert result == "205.00"

def test_interest_tier3_deposit():
    result = calculate_interest(61000)
    assert result == "2380.00"


def test_interest_tier4_deposit():
    result = calculate_interest(130000)
    assert result == "5290.00"

#Invalid partitions
def test_negative_deposit():
    with pytest.raises(ValueError, match="Deposit cannot be negative"):
        calculate_interest(-55)


def test_string_input():
    with pytest.raises(ValueError, match="Deposit must not be a string"):
        calculate_interest("1000")


def test_boolean_input():
    with pytest.raises(ValueError, match="Deposit must not be a Boolean"):
        calculate_interest(True)


def test_list_input():
    with pytest.raises(ValueError, match="Deposit must be a number"):
        calculate_interest([1000])


def test_none_input():
    with pytest.raises(ValueError, match="Deposit must be a number"):
        calculate_interest(None)


def test_float_input():
    result = calculate_interest(1500.50)
    assert result == "47.52"